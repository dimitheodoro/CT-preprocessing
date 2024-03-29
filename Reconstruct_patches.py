from patchify import  unpatchify


def reconstruct(image, patient_number=1,slice=100):
        original=image[patient_number][:,:,:,slice]
        original=original.reshape(4,4,128,128)
        return unpatchify(original,(512,512))

