import hashlib

hash_to_crack = input("Hash to crack: \n")
# hash_to_crack = "9e88d81f036dad3e1f7d3e947fdf291df2606a3b3c5bd1f8201104bc47ca16cc"
path_to_dictionary = input("Wordlist location: \n")
# path_to_dictionary = ["bannanums"]


def try_passwords(hash_to_crack, path_to_dictionary):
    with open(path_to_dictionary, "r") as file:
        for password in file.readlines():
            hashed_pw = hashlib.sha3_256(password.strip().encode()).hexdigest()
            if hashed_pw == hash_to_crack:
                return password.strip()
    return "Pass not found"


result = try_passwords(hash_to_crack, path_to_dictionary)
print(result)
