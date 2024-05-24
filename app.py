import pickle as pkl
import numpy as np

def load_model():
    file = open('model.pkl','rb')
    data = pkl.load(file)
    return data['model']


'''
Data for testing the model, either it is predecting or not!!

test_data = np.array([-1.35980713e+00, -7.27811733e-02,  2.53634674e+00,  1.37815522e+00, -3.38320770e-01,  4.62387778e-01,  2.39598554e-01,  9.86979013e-02, 3.63786970e-01,  9.07941720e-02, -5.51599533e-01, -6.17800856e-01, -9.91389847e-01, -3.11169354e-01,  1.46817697e+00, -4.70400525e-01, 2.07971242e-01,  2.57905802e-02,  4.03992960e-01,  2.51412098e-01, -1.83067779e-02,  2.77837576e-01, -1.10473910e-01,  6.69280749e-02, 1.28539358e-01, -1.89114844e-01,  1.33558377e-01, -2.10530535e-02, 1.49620000e+02]).reshape(1,-1)
prediction = model.predict(test_data)[0]
print(prediction)

Boom!!, Its working good with an accuracy of 97%
'''

def modelPrediction(model):
    print('Enter the following Values to make a successfull Predection\n');
    input_arr = [];
    for i in range(28):
        input_arr.append(float(input(f'Enter the value of V{i+1} PCA Field: ')))

    input_arr.append(float(input('Enter the value of Transaction Amount: ')));

    predicted_value = model.predict(np.array(input_arr).reshape(1,-1))[0]

    print(f'\nThe Transaction is {predicted_value}\n\n')


def InitializeConsole():
    model = load_model();
    print('\nCredit Card Fraud Detection System\n\n')
    while True:
        modelPrediction(model)
        inp = input('Press T/t to try again or any other key to exit: ')
        if(inp!='T' and inp!='t'):
            break


InitializeConsole()

        



