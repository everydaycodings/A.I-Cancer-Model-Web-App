from django.shortcuts import render, HttpResponse
import pickle
import math
# Create your views here.

def index(request):

    pickle_in = open("Breast_Cancer/Cancer_model.pickle", "rb")
    linear = pickle.load(pickle_in)

    context = {}

    if request.method == "POST":
        clump_thickness = int(request.POST["clump_thickness"])
        cell_size = int(request.POST["cell_size"])
        cell_shape = int(request.POST["cell_shape"])
        marginal_adhesion = int(request.POST["marginal_adhesion"])
        s_e_c_s = int(request.POST["s_e_c_s"])
        nuclei = int(request.POST["nuclei"])
        chromatin = int(request.POST["chromatin"])
        n_nucleoli = int(request.POST["n_nucleoli"])
        mitoses = int(request.POST["mitoses"])

        customValue = [
            [clump_thickness, cell_size, cell_shape, marginal_adhesion, s_e_c_s, nuclei, chromatin, n_nucleoli, mitoses]]

        predictions = linear.predict(customValue)
        final_prediction = math.trunc(int(predictions))
        print(final_prediction)

        if final_prediction == 0:
            print("Not Having Cancer")
            print("Predicted Value:", predictions)
        if final_prediction == 1:
            print("Having Cancer")
            print("Predicted_Value: ", predictions)

        context = {"predictions": predictions, "final_prediction": final_prediction}


        
    return render (request, "Breast_Cancer/index.html")