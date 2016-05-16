# NetworkSimulator
Developed the router simuator using FIFO queues and various QoS paramenters were taken into consideration.
1.Read PCAP files containing IPV4 packets
2.Extracted each packet's destination address
3.Masked the destination address of each packet with the destination address of the routing table
4.Performed longest prefix match.
5.Controlled the speed of reading and writing to the queues to ensure QoS.
6.Checked DSCP value and ensured forwarding in that order
7.Packets written out at for the intended output port in the binary form
