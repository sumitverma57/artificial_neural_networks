inputs=[0,1]
weights=[1]
Required_Output=[]
Net_Input=[]
Predicted_Output=[]
def real_NOT_output():
    for value in inputs:
        if value == 0:
            Required_Output.append(1)
        else:
            Required_Output.append(0)
def NOT_logic_computation():
    for value in inputs:
        Net_Input.append(value*weights[0])
def final_output_computation():
    for value in Yin:
        if value >= 1:
            Predicted_Output.append(0)
        else:
            Predicted_Output.append(1)
if __name__ == '__main__':
    real_NOT_output()
    NOT_logic_computation()
    final_output_computation()
    print "   Logic NOT\n"
    print "\x1B[3mx1\x1B[23m","\x1B[3mNet_Input\x1B[23m","\x1B[3mPredicted_Output\x1B[23m","\x1B[3mRequired_Output\x1B[23m"
    for i in range(len(inputs)):
        print inputs[i],"   ",Net_Input[i],"          ",Predicted_Output[i],"         ",Required_Output[i]
