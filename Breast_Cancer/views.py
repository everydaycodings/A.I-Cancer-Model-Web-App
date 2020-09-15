from django.shortcuts import render, HttpResponse
import pickle
import math
# Create your views here.

def index(request):


    pickle_in = open("Breast_Cancer/Cancer_model.pickle", "rb")
    linear = pickle.load(pickle_in)

    print("All The Values Will Be Between 1-10")
    clump_thickness = int(input("Clump_Thickness: "))
    cell_size = int(input("Cell_Size: "))
    cell_shape = int(input("Cell_Shape: "))
    marginal_adhesion = int(input("Marginal_Adhesion: "))
    s_e_c_s = int(input("single_Epithelial_Cell_Size: "))
    nuclei = int(input("Bare_Nuclei: "))
    chromatin = int(input("Bland_Chromatin: "))
    n_nucleoli = int(input("Normal_Nucleoli: "))
    mitoses = int(input("Mitoses: "))

    customValue = [
        [clump_thickness, cell_size, cell_shape, marginal_adhesion, s_e_c_s, nuclei, chromatin, n_nucleoli, mitoses]]

    predictions = linear.predict(customValue)
    final_prediction = math.trunc(int(predictions))

    print()
    if final_prediction == 0:
        print("Not Having Cancer")
        print("Predicted Value:", predictions)
    if final_prediction == 1:
        print("Having Cancer")
        print("Predicted_Value: ", predictions)


    return render (request, "Breast_Cancer/index.html")