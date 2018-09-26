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

    # #def random_email_addresses():
    # for i in range(len(random_email_array_with_duplicates)):
    #     random_email_string = random_email_string + str(random_email_array_with_duplicates[i])

    return random_email_string
print(create_random_email_string())