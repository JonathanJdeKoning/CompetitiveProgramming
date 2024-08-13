def printmove(x,y):
    return "{" + f'"type":"move","target_x":{x},"target_y":{y}' + "}"


def printattack(id):
    return "{" + f'"type":"attack","target_id":{id}' + "}"

