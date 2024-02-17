
import numpy as np

def accuracy_patient_level(model,patients_test_patches,y_test,labels_sex_test_patches,labels_age_test_patches,labels_GCS_test_patches):

    test_predictions_array = []
    for PATIENT_NUM in range(patients_test_patches.shape[0]):

        test_predictions_array.append( model.predict([patients_test_patches[PATIENT_NUM],
                                                labels_sex_test_patches[PATIENT_NUM],labels_age_test_patches[PATIENT_NUM],
                                                labels_GCS_test_patches[PATIENT_NUM]]))
    def predict(arr):
        MEAN = np.mean(arr)
        if MEAN > 0.5:
            return 1
        else:
            return 0
    test_predictions = []

    for PATIENT_NUM in range(patients_test_patches.shape[0]):
        test_predictions.append(predict(test_predictions_array[PATIENT_NUM]))

    positives = 0
    negatives = 0
    for PATIENT_NUM in range(patients_test_patches.shape[0]):
        if test_predictions[PATIENT_NUM]==y_test[PATIENT_NUM][0]:
            positives +=1
        else:
            negatives +=1
    
    accuracy = positives/patients_test_patches.shape[0]
    return accuracy