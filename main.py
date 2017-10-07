import boto3
import writer
value = raw_input("Enter retrieved value:  ")
writer.ProcessandPrint(int(value))

