import uuid

print(uuid.uuid1())
print(uuid.uuid1())
print("--------------------")
# print(uuid.uuid2())
# print(uuid.uuid2())
# import uuid
# import os

# def generate_uuid2():
#     uid = os.getuid()  # Get the current POSIX UID (user ID)
#     gid = os.getgid()  # Get the current POSIX GID (group ID)
#     timestamp = int(os.times()[4])  # Get the current timestamp (usually in seconds)
    
#     # Combine UID, GID, and timestamp to create a UUID2
#     uuid2 = uuid.UUID(int=(uid << 32) | (gid << 16) | timestamp)
#     return uuid2

# # Generate and print UUID2
# uuid2 = generate_uuid2()
# print("UUID2:", uuid2)

# print(uuid.uuid3())
print("--------------------")
print(uuid.uuid4())
print(uuid.uuid4())
 

print("-------------------------------uuid3------------------------")
import uuid

# Define a namespace (it can be any valid UUID)
namespace = uuid.UUID('6ba7b810-9dad-11d1-80b4-00c04fd430c8')

# Define a name for which you want to generate a UUID3
name = 'example.com'

# Generate UUID3 based on the namespace and name using MD5 hash
uuid3 = uuid.uuid3(namespace, name)

# Print the generated UUID3
print("UUID3:", uuid3)

