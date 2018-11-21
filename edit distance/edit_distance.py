
def minimum(v1 ,v2 ,v3):
    temp = 0 ;
    if v2 < v3 :
        temp = v2;
    else :
        temp = v3
    if v1 < temp:
        return v1
    return temp;

def compaireStr(s1 ,s2):
    if(s1[len(s1)-1] == s2[len(s2)-1]):
        return 0;
    else :
        return 1;
    
def edit_distance(src , target):
    
    src_len = len(src);
    target_len = len(target)
    array = []
    for i in range(src_len +1):
        array.append([0] * (target_len+1))

    for i in range(src_len +1):
        array[i][0] = i;
    for i in range(target_len+1):
        array[0][i] = i;
    
    for i in range(src_len) :
        for  j in range(target_len):
            array[i+1][j+1] = minimum(
                array[i][j]  + compaireStr(src[0:i+1], target[0:j+1]),
                array[i][j+1]  +1,
                array[i+1][j]  + 1
            )
            print(array)
            
    

    return array[src_len][target_len ];


src = input( "source string : ");
target = input( "target string : ");

print(edit_distance(src, target));
