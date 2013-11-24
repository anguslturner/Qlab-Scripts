from pythonosc import osc_message_builder
from pythonosc import udp_client

ip = input("IP Address of QLab Machine (127.0.0.1): ")
if not ip:
    ip = '127.0.0.1'

file = open(input("File Path:"), 'r')
client = udp_client.UDPClient(ip, 53000)

for line in file:
    #Uses format type / q name / target / post wait / video effect / text
    parsed = line.split(" / ")
    
    msg = osc_message_builder.OscMessageBuilder(address = '/new')
    msg.add_arg(parsed[0])
    msg = msg.build()
    client.send(msg)
    
    msg = osc_message_builder.OscMessageBuilder(address = '/cue/selected/name')
    msg.add_arg(parsed[1])
    msg = msg.build()
    client.send(msg)
    
    msg = osc_message_builder.OscMessageBuilder(address = '/cue/selected/fileTarget')
    msg.add_arg(parsed[2])
    msg = msg.build()
    client.send(msg)
    
    msg = osc_message_builder.OscMessageBuilder(address = '/cue/selected/postWait')
    msg.add_arg(int(parsed[3]))
    msg = msg.build()
    client.send(msg)
    
    msg = osc_message_builder.OscMessageBuilder(address = '/cue/selected/doEffect')
    msg.add_arg(1)
    msg = msg.build()
    client.send(msg)
    
    msg = osc_message_builder.OscMessageBuilder(address = '/cue/selected/effect')
    msg.add_arg(32) #titles
    msg = msg.build()
    client.send(msg)
    
    msg = osc_message_builder.OscMessageBuilder(address = '/cue/selected/effectSet')
    msg.add_arg('Text')
    msg.add_arg(parsed[5])
    msg = msg.build()
    client.send(msg)