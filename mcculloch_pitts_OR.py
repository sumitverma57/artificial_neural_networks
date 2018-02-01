inputs=[[0,0],[0,1],[1,0],[1,1]]
weights=[1,1]
Required_Output=[]
Net_Input=[]
Predicted_Output=[]
def real_OR_output():
    for value in inputs:
        if value[0] and value[1]==1:
            Required_Output.append(value[0])
        else:
            Required_Output.append(value[0]+value[1])
def OR_logic_computation():
    for value in inputs:
        Net_Input.append(value[0]*weights[0]+value[1]*weights[1])
def final_output_computation():
    for value in Yin:
        if value >= 1:
            Predicted_Output.append(1)
        else:
            Y.append(0)
if __name__ == '__main__':
    real_OR_output()
    OR_logic_computation()
    final_output_computation()
    print "   Logic OR\n"
    print "\x1B[3mx1\x1B[23m","\x1B[3mx2\x1B[23m","\x1B[3mNet_Input\x1B[23m","\x1B[3mPredicted_Output\x1B[23m","\x1B[3mRequired_Output\x1B[23m"
    for i in range(len(inputs)):
        print inputs[i][0]," ",inputs[i][1],"   ",Net_Input[i],"          ",Predicted_Output[i],"         ",Required_Output[i]
