# BlueBerry Pie
# Copy Feature Classes and Feature Datasets
# Date: 02/06/2018
# Developed by Louie Padilla

"""
Takes a template of a feature dataset and copies it into another location. Asks the user how many datasets to make and
name them accordingly

"""
# Import system modules
import arcpy
import os

# Set the workspace for ListFeatureClasses
# Location of feature class template to copy from
template_feature_set = arcpy.env.workspace = arcpy.GetParameterAsText(0)

# Use the ListFeatureClasses function to return a list of shapefiles.
featureclasses = arcpy.ListFeatureClasses()
# Set local variables

# Ask user how many feature sets to create, start number count is 1
num_count = 1
end_count = int(arcpy.GetParameterAsText(1))

# Location of feauture set
# Ask user for location
out_database_path = arcpy.GetParameterAsText(2)


# Makes copies of feature classes in a feature dataset
# Paste the copied feature classes to new location
def copy_features(name):
    try:
        for fc in featureclasses:
            feature_class_name = fc.replace("_", "{}_".format(str(num_count).zfill(2)))
            print(feature_class_name)
            arcpy.CopyFeatures_management(fc, os.path.join(name, feature_class_name))
    except:
        print("{} Feature class already exist".format(name))


# Creates a dataset if has not been made
# If made, that is the location of where the feature classes will be copied into
def create_dataset(name):
    global out_database_path
    try:
        arcpy.CreateFeatureDataset_management(out_database_path, name, template_feature_set)
        print ("Making dataset {}".format(name))
        arcpy.AddMessage("Making dataset {}".format(name))
    except:
        print("{} Dataset already exist".format(name))
        arcpy.AddMessage("{} Dataset already exist".format(name))
    dataset = "{}\{}".format(out_database_path, name)
    return dataset


########################################################################################################################

# Will copy features until count reaches user's number input
while num_count <= end_count:
    FMA_Name = "FMA{}".format(str(num_count).zfill(2))
    name = create_dataset(FMA_Name)
    copy_features(name)
    num_count += 1

print("Task Complete!")
