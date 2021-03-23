import scapy.all as scapy
import optparse

def get_user_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-r","--range",dest="user_range",help="Enter a range")

    (user_input,arguments) = parse_object.parse_args()

    if not user_input.user_range:
        print("Enter a range!")

    return user_input

def scan_my_network(usr_range):
    arp_request_packet = scapy.ARP(pdst=usr_range)
    #scapy.ls(scapy.ARP())
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    #scapy.ls(scapy.Ether())

    combined_packet = broadcast_packet/arp_request_packet
    (answered_list,unanswered_list) = scapy.srp(combined_packet,timeout=1)
    answered_list.summary()

user_range_input = get_user_input()
scan_my_network(user_range_input.user_range)
