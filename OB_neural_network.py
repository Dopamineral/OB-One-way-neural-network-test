import random
 
class Neuron:
    def __init__(self,downstream_partner_list,downstream_partner_weights,downstream_partner_values,current_value):
        self.downstream_partner_list = downstream_partner_list
        self.downstream_partner_weights = downstream_partner_weights
        self.downstream_partner_values = downstream_partner_values
        self.current_value = current_value
        
    def create_connection_weights(self,layerlist):
        self.downstream_partner_weights = []
        for i in range(len(self.downstream_partner_list)):
            self.downstream_partner_weights.append(layerlist[i] + (random.random()/10))
        return self.downstream_partner_weights
            
    def sum_partners(self):
        for i in range(len(self.downstream_partner_list)):
            x = self.downstream_partner_values[i]
            y = self.downstream_partner_weights[i]
            partner_value = x*y          
            self.current_value = self.current_value + partner_value
        print(self.current_value)
        return self.current_value
    
    def add_to_layer_list(self,layerlist):
        layerlist = layerlist.append(self.current_value)
        

            
#Layer1 --------------------------------------
##############################################  
print("Layer1")
 
 
N1_1 = Neuron([],[],[],10)
N1_2 = Neuron([],[],[],20)
N1_3 = Neuron([],[],[],30)
N1_4 = Neuron([],[],[],10)
N1_5 = Neuron([],[],[],20)
N1_6 = Neuron([],[],[],30)
N1_7 = Neuron([],[],[],10)
N1_8 = Neuron([],[],[],20)
N1_9 = Neuron([],[],[],30)

layer1_values = []
layer1_weights = [0.1, #Neuron1
                  0.2, #Neuron2
                  0.3, #Neuron3
                  0.2, #Neuron4
                  0.1, #Neuron5
                  0.1, #Neuron6
                  0.3, #Neuron7
                  0.4, #Neuron8
                  0.2, #Neuron9
                  ]
layer1_partners = [N1_1,
                       N1_2,
                       N1_3,
                       N1_4,
                       N1_5,
                       N1_6,
                       N1_7,
                       N1_8,
                       N1_9]

N1_1.add_to_layer_list(layer1_values)
N1_2.add_to_layer_list(layer1_values)
N1_3.add_to_layer_list(layer1_values)
N1_4.add_to_layer_list(layer1_values)
N1_5.add_to_layer_list(layer1_values)
N1_6.add_to_layer_list(layer1_values)
N1_7.add_to_layer_list(layer1_values)
N1_8.add_to_layer_list(layer1_values)
N1_9.add_to_layer_list(layer1_values)


                  



                   
#Layer2 --------------------------------------
##############################################
print("Layer2")
layer2_weights = [0.1, #Neuron1
                  0.2, #Neuron2
                  0.3, #Neuron3
                  0.2, #Neuron4
                  0.1, #Neuron5
                  0.1, #Neuron6
                  0.3, #Neuron7
                 ]

layer2_values = []

N2_1 = Neuron(layer1_partners,layer1_weights,layer1_values,0)
N2_2 = Neuron(layer1_partners,layer1_weights,layer1_values,0)
N2_3 = Neuron(layer1_partners,layer1_weights,layer1_values,0)
N2_4 = Neuron(layer1_partners,layer1_weights,layer1_values,0)
N2_5 = Neuron(layer1_partners,layer1_weights,layer1_values,0)
N2_6 = Neuron(layer1_partners,layer1_weights,layer1_values,0)
N2_7 = Neuron(layer1_partners,layer1_weights,layer1_values,0)

#N2_1.create_connection_weights(layer1_weights)
#N2_2.create_connection_weights(layer1_weights)
#N2_3.create_connection_weights(layer1_weights)
#N2_4.create_connection_weights(layer1_weights)
#N2_5.create_connection_weights(layer1_weights)
#N2_6.create_connection_weights(layer1_weights)
#N2_7.create_connection_weights(layer1_weights)

layer2_partners = [N2_1,
                   N2_2,
                   N2_3,
                   N2_4,
                   N2_5,
                   N2_6,
                   N2_7,
                   ]

N2_1.sum_partners()
N2_2.sum_partners()
N2_3.sum_partners()
N2_4.sum_partners()
N2_5.sum_partners()
N2_6.sum_partners()
N2_7.sum_partners()

N2_1.add_to_layer_list(layer2_values)
N2_2.add_to_layer_list(layer2_values)
N2_3.add_to_layer_list(layer2_values)
N2_4.add_to_layer_list(layer2_values)
N2_5.add_to_layer_list(layer2_values)
N2_6.add_to_layer_list(layer2_values)
N2_7.add_to_layer_list(layer2_values)

#Layer3 --------------------------------------
##############################################
print("Layer3")
layer3_weights = [0.5, #Neuron1
                  0.4, #Neuron2
                  0.2, #Neuron3
                  ]

layer3_values = []

N3_1 = Neuron(layer2_partners,layer2_weights,layer2_values,0)
N3_2 = Neuron(layer2_partners,layer2_weights,layer2_values,0)
N3_3 = Neuron(layer2_partners,layer2_weights,layer2_values,0)

layer3_partners = [N3_1,
                   N3_2,
                   N3_3,
                   ]

#N3_1.create_connection_weights(layer2_weights)
#N3_2.create_connection_weights(layer2_weights)
#N3_3.create_connection_weights(layer2_weights)


N3_1.sum_partners()
N3_2.sum_partners()
N3_3.sum_partners()

N3_1.add_to_layer_list(layer3_values)
N3_2.add_to_layer_list(layer3_values)
N3_3.add_to_layer_list(layer3_values)

#Layer4 --------------------------------------
##############################################
print("Layer4")
layer4_weights = [1, #Neuron1          
                  ]

layer4_values = []

N4_1 = Neuron(layer3_partners,layer3_weights,layer3_values,0)

layer4_partners = [N4_1,
                   ]
#N4_1.create_connection_weights(layer3_weights)

N4_1.sum_partners()

N4_1.add_to_layer_list(layer4_values)

###############################################################################
