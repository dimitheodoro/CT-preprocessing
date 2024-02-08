import Levenshtein
import os

def find_similar_names(name, name_list, threshold=0.04):
    similar_names = []
    for n in name_list:
        distance = Levenshtein.distance(name.lower(), n.lower())
        similarity = 1 - (distance / max(len(name), len(n)))
        if similarity >= threshold:
            similar_names.append((n, similarity))
    similar_names.sort(key=lambda x: x[1], reverse=True)  # Sort by similarity score
    return similar_names

def main():
    provided_name = input("Enter the name to check similarity: ")
    similar_names_all_scans = find_similar_names(provided_name, ALL_SCANS)
    similar_names_all_scans2 = find_similar_names(provided_name, ALL_SCANS2)
    similar_names_all_scans3 = find_similar_names(provided_name, ALL_SCANS3)

    print("\nSimilar names in {}:".format(folder1))
    for name, similarity in similar_names_all_scans:
        print(f"{name} (Similarity: {similarity:.2f})")

    print("\nSimilar names in {}:".format(folder2))
    for name, similarity in similar_names_all_scans2:
        print(f"{name} (Similarity: {similarity:.2f})")

    print("\nSimilar names in {}:".format(folder3))
    for name, similarity in similar_names_all_scans3:
        print(f"{name} (Similarity: {similarity:.2f})")

if __name__ == "__main__":
    folder1='ALL SCANS'
    folder2='ALL SCANS2'
    folder3='ALL SCANS3'
    DESKTOP_PATH =r'C:\Users\aktinologiko\Desktop'

    PATH_WITH_ALL_SCANS = os.path.join(DESKTOP_PATH,folder1)
    PATH_WITH_ALL_SCANS2 = os.path.join(DESKTOP_PATH,folder2)
    PATH_WITH_ALL_SCANS3 = os.path.join(DESKTOP_PATH,folder3)

    ALL_SCANS = os.listdir(PATH_WITH_ALL_SCANS)
    ALL_SCANS2 = os.listdir(PATH_WITH_ALL_SCANS2)
    ALL_SCANS3 = os.listdir(PATH_WITH_ALL_SCANS3)
    main()
