text = "We are learning Python for Devops"
new_text = text.split( )
print(new_text)

arn = "arn:partition:service:region:account-id:resource-type/resource-id"
new_arn = arn.split("/")
print("Display arn:", new_arn)
print(arn.split("/")[1])