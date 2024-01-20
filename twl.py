import pyperclip
suffix = ".wikipedialibrary.idm.oclc.org"

def twlToNormal(linkIn):
    linkList = linkIn.split(suffix)
    linkList[0] = linkList[0].replace("-",".")
    linkOut = linkList[0] + linkList [1]
    return linkOut

def normalToTWL(linkIn):
    linkOut = "https://" + suffix[1:] + "/login?url=" + linkIn  # the [1:] removes the first character of the string
    return linkOut


while True:
    inp = input("Enter link to convert: ")

    if suffix in inp:
        output = twlToNormal(inp)
    else:
        output = normalToTWL(inp)

    pyperclip.copy(output)
    print(output)
    print("Copied to clipboard.\n")
