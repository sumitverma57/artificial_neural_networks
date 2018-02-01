inputs=[[0,0],[0,1],[1,0],[1,1]]
weights=[1,1]
Required_Output=[]
Net_Input=[]
Predicted_Output=[]
def real_AND_output():
    for value in inputs:
        Required_Output.append(value[0]*value[1])
def AND_logic_computation():
    for value in inputs:
        Net_Input.append(value[0]*weights[0]+value[1]*weights[1])
def final_output_computation():
    for value in Yin:
        if value >= 2:
            Predicted_Output.append(1)
        else:
            Predicted_Output.append(0)
if __name__ == '__main__':
    real_AND_output()
    AND_logic_computation()
    final_output_computation()
    print "  Logic AND\n"
    print "\x1B[3mx1\x1B[23m","\x1B[3mx2\x1B[23m","\x1B[3mNet_Input\x1B[23m","\x1B[3mPredicted_Output\x1B[23m","\x1B[3mRequired_Output\x1B[23m"
    for i in range(len(inputs)):
        print inputs[i][0]," ",inputs[i][1],"   ",Net_Input[i],"          ",Predicted_Output[i],"         ",Yreq[i]
