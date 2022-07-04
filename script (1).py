from mininet.topo import Topo
import json

class CustomTopo(Topo):

    def build(self, n_switches=9, n_hosts=11):

        #Load struct from file
        links = []
        with open("struct_config.json", 'r') as struct_info:
            links = json.load(struct_info)

        # Build objects
        #self.objects["c1"] = self.addController('c1') 
        self.objects = dict()
        for h in range(n_hosts):
            host_label = 'h%s' % (h+1)
            self.objects[host_label] = self.addHost(host_label)     
        for s in range(n_switches):
            switch_label = 's%s' % (s+1)
            self.objects[switch_label] = self.addSwitch(switch_label)
    
        # Link objects
        for link in links:
            try:
                left_label, right_label = link[0], link[1]
                left_object = self.objects[left_label]
                right_object = self.objects[right_label]
                self.addLink(left_object, right_object)
            except KeyError:
                print("ERROR: %s and/or %s are not valid objects." % (left_label,right_label))

topos = {'customtopo': (lambda: CustomTopo())}