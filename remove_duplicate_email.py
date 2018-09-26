import json

def create_random_email_string():

    import random

    def create_random_email():
        
        random_numbers = ""
        
        random_letters = ""
        
        for i in range(0,5):
            random_numbers = random_numbers + str(random.randint(1,5))
        
        for i in range(len(random_numbers)):
            if random_numbers[i] == "1":
                random_letters = random_letters + "a"
            if random_numbers[i] == "2":
                random_letters = random_letters + "b"
            if random_numbers[i] == "3":
                random_letters = random_letters + "c"
            if random_numbers[i] == "4":
                random_letters = random_letters + "d"
            if random_numbers[i] == "5":
                random_letters = random_letters + "e"
        return (random_letters + "@gmail.com")
        
    random_email_array = []
    random_email_array_with_duplicates = random_email_array

    for i in range(0,5):
        random_email_array.append(create_random_email())


    random_email_array_with_duplicates.append(random_email_array[4])
    random_email_array_with_duplicates.append(random_email_array[2])

    random_email_string = ",".join(random_email_array_with_duplicates)

    return random_email_string

with open("remove_duplicate_email.json","r") as file_object:
    email_list = str(json.load(file_object))

email_list = email_list + create_random_email_string()

with open("remove_duplicate_email.json","w") as file_object:
    json.dump(email_list,file_object)


email_list = ""

with open("remove_duplicate_email.json","r") as file_object:
    email_list = str(json.load(file_object))


email_list_with_duplicates_array = email_list.split(",")
email_list_without_duplicates_array = [i for idx, i in enumerate(email_list_with_duplicates_array) if i not in email_list_with_duplicates_array[:idx]]

print(email_list_with_duplicates_array)
print(email_list_without_duplicates_array)

print(len(email_list_with_duplicates_array))
print(len(email_list_without_duplicates_array))

with open("email_duplicates_removed.json","w") as file_object:
    json.dump(email_list_without_duplicates_array,file_object)
