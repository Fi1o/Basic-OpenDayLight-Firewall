
package main 

import (
	"encoding/xml"
	"io/ioutil"
	"C"
)

 


type input struct {
	Xmlns   string `xml:"xmlns,attr"`
	Barrier string `xml:"barrier"`
	Node1   Node   `xml:"node"`
	Cookie  string `xml:"cookie"`
	Flags   string `xml:"flags"`
	HardTO  string `xml:"hard-timeout"`
	IdleTO  string `xml:"idle-timeout"`
	InstHW  string `xml:"installHw"`	
	EType   string `xml:"match>ethernet-match>ethernet-type>type"`
	IPDest  string `xml:"match>ipv4-destination"`
	IPSrc   string `xml:"match>ipv4-source"`
	IpProt	string `xml:"match>ip-match>ip-protocol"`
	TcpSrc	string `xml:"match>tcp-source-port"`
	TcpDst	string `xml:"match>tcp-destination-port"`
	Order1  string `xml:"instructions>instruction>order"`
	Order2  string `xml:"instructions>instruction>apply-actions>action>order"`
	Drop    string `xml:"instructions>instruction>apply-actions>action>drop-action"`
	Pri     string `xml:"priority"`
	Strict  string `xml:"strict"`	
    TableID string `xml:"table_id"`
}
 
type Node struct  {
	Xmlns2  string `xml:"xmlns:inv,attr"`
	Node1   string `xml:",chardata"`
}
//export Goflowgo
func Goflowgo(srcIP, dstIP, srcTcp, dstTcp string) {
	note := &input{
		Xmlns:   "urn:opendaylight:flow:service",
		Barrier: "false",
		Node1:    Node{"urn:opendaylight:inventory","/inv:nodes/inv:node[inv:id=\"openflow:66160483355520\"]"},
		Cookie:  "55",
		Flags:    "SEND_FLOW_REM",
		HardTO:  "0",
		IdleTO:  "0",
		InstHW:  "false",
		EType:   "2048",
		IPDest:  dstIP,
		IPSrc:	 srcIP,
		TcpSrc:	 srcTcp,
		TcpDst:	 dstTcp,
		IpProt:  "6",
		Order1:  "0",
		Order2:  "0",
		TableID: "0",
		Strict:  "false",
		Pri:     "11",
	}
	
 
	file, _ := xml.MarshalIndent(note, "", " ")

	file =  []byte(xml.Header + string(file))
    var fileName = "flow.xml"
	_ = ioutil.WriteFile(fileName, file, 0644)
 
}
func main() {}
