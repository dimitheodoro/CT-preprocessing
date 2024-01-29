
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Concatenate,Reshape,Embedding, Input,Conv2D, MaxPooling2D, Flatten, Dense, Dropout



def MultipleInputsModel(input_shape, sex_label_shape, age_label_shape,GCS_label_shape, sex_num_classes=2, age_num_classes=3,GCS_num_classes=3):
    # Functional API
    sex_label =Input(sex_label_shape)  #shape=(1,)
    sex = Embedding (sex_num_classes,50)(sex_label)
    n_nodes = input_shape[0] * input_shape[1] 
    sex = Dense(n_nodes)(sex)
    sex_out = Reshape((input_shape[0],input_shape[1],1))(sex)

    age_label =Input(age_label_shape)
    age = Embedding (age_num_classes,50)(age_label)
    age = Dense(n_nodes)(age)
    age_out = Reshape((input_shape[0],input_shape[1],1))(age)

    GCS_label =Input(GCS_label_shape)
    GCS = Embedding (GCS_num_classes,50)(GCS_label)
    GCS = Dense(n_nodes)(GCS)
    GCS_out = Reshape((input_shape[0],input_shape[1],1))(GCS)


    merge_embed = Concatenate()([sex_out,age_out,GCS_out])
    input_image = Input(shape=input_shape)
    merge = Concatenate()([input_image,merge_embed])
    x = Conv2D(32, (3, 3), activation='relu')(merge)
    x = MaxPooling2D((2, 2))(x)
    x = Conv2D(64, (3, 3), activation='relu')(x)
    x = MaxPooling2D((2, 2))(x)
    x = Conv2D(128, (3, 3), activation='relu')(x)
    x = MaxPooling2D((2, 2))(x)
    x = Conv2D(128, (3, 3), activation='relu')(x)
    x = MaxPooling2D((2, 2))(x)
    x = Flatten()(x)
    x = Dense(512, activation='relu')(x)
    x = Dropout(0.5)(x)
    output_layer = Dense(1, activation='sigmoid')(x)
    # Create the model
    model = Model([input_image,sex_label,age_label,GCS_label], outputs=output_layer)
    # Compile the model
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model




# def MultipleInputsModel(input_shape, sex_label_shape, age_label_shape,sex_num_classes=2, age_num_classes=3 ):
#     # Functional API
#     sex_label =Input(sex_label_shape)  #shape=(1,)
#     sex = Embedding (sex_num_classes,50)(sex_label)
#     n_nodes = input_shape[0] * input_shape[1] 
#     sex = Dense(n_nodes)(sex)
#     sex_out = Reshape((input_shape[0],input_shape[1],1))(sex)

#     age_label =Input(age_label_shape)
#     age = Embedding (age_num_classes,50)(age_label)
#     age = Dense(n_nodes)(age)
#     age_out = Reshape((input_shape[0],input_shape[1],1))(age)

#     merge_embed = Concatenate()([sex_out,age_out])
#     input_image = Input(shape=input_shape)
#     merge = Concatenate()([input_image,merge_embed])
#     x = Conv2D(32, (3, 3), activation='relu')(merge)
#     x = MaxPooling2D((2, 2))(x)
#     x = Conv2D(64, (3, 3), activation='relu')(x)
#     x = MaxPooling2D((2, 2))(x)
#     x = Conv2D(128, (3, 3), activation='relu')(x)
#     x = MaxPooling2D((2, 2))(x)
#     x = Conv2D(128, (3, 3), activation='relu')(x)
#     x = MaxPooling2D((2, 2))(x)
#     x = Flatten()(x)
#     x = Dense(512, activation='relu')(x)
#     x = Dropout(0.5)(x)
#     output_layer = Dense(1, activation='sigmoid')(x)
#     # Create the model
#     model = Model([input_image,sex_label,age_label], outputs=output_layer)
#     # Compile the model
#     model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
#     return model





