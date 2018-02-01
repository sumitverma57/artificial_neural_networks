inputs=[[1,1],[1,-1],[-1,1],[-1,-1]]
weights=[0,0]
alpha=1
b=0
Net_Input=[None]*4
Required_Output=[]
Predicted_Output=[None]*4
def logic_OR_output():
    for value in inputs:
        if (value[0]==-1) and (value[1]==-1):
            Required_Output.append(-1)
        else:
            Required_Output.append(1)
def net_input_computation(i):
    Net_Input[i]=(b+weights[0]*inputs[i][0]+weights[1]*inputs[i][1])
def final_predicted_output(i):
    if Net_Input[i]>=0:
        Predicted_Output[i]=(1)
    else:
        Predicted_Output[i]=(-1)
def update_weights(i):
    weights[0]=weights[0]+(alpha*Required_Output[i]*inputs[i][0])
    weights[1]=weights[1]+(alpha*Required_Output[i]*inputs[i][1])
    global b
    b=b+(alpha*Required_Output[i])

def predicted_compare_required(i):
    if Predicted_Output[i]!=Required_Output[i]:
        print "updation of weights required!!\n"
        update_weights(i)
        print "new weights\n",weights[0],weights[1],b
        net_input_computation(i)
        final_predicted_output(i)
        predicted_compare_required(i)
    else:
        print "Predicted_Output","=",Predicted_Output[i],"==","Required_Output","=",Required_Output[i]

if __name__ == '__main__':
    logic_OR_output()
    print Required_Output
    #first epoch
    print "\x1B[3m\nfirst epoch\x1B[23m"
    net_input_computation(0)
    final_predicted_output(0)
    predicted_compare_required(0)

    #second epoch
    print "\x1B[3m\nsecond epoch\x1B[23m"
    net_input_computation(1)
    final_predicted_output(1)
    predicted_compare_required(1)

    #third epoch
    print "\x1B[3m\nthird epoch\x1B[23m"
    net_input_computation(2)
    final_predicted_output(2)
    predicted_compare_required(2)

    #fourth epoch
    print "\x1B[3m\nfourth epoch\x1B[23m"
    net_input_computation(3)
    final_predicted_output(3)
    predicted_compare_required(3)
