from protobuf import blockchain_pb2

query = blockchain_pb2.StateQuery()

key = b"_sv_VarName-\xfe"
query.storageKeys.append(str(key))

serialized = query.SerializeToString()
print("key        = ", key)
print("serialized = ", serialized)
