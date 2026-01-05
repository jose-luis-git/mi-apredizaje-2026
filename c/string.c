#include<stdio.h>
#include<string.h>
#include<ctype.h>

void clearNewLine(char*);
void equalString(char*,char*);
void longerString(char*,char*);
void concatenateString(char*,char*);
void mayusString(char*,char*);

int main(){
    char name1[50], name2[50];
    printf("Enter a name: ");
    fgets(name1, sizeof(name1), stdin);
    clearNewLine(name1);
    printf("Enter another name: ");
    fgets(name2, sizeof(name2), stdin);
    clearNewLine(name2);

    equalString(name1, name2);
    longerString(name1, name2);
    concatenateString(name1, name2);
    mayusString(name1, name2);

    return 0;
}
void clearNewLine(char*name){
    name[strcspn(name, "\n")] = '\0';
}
void equalString(char*name1, char*name2){
    if(strcmp(name1, name2) == 0){
        printf("\nThe name %s and name %s are the same", name1,name2);
    }else{
        printf("The names are not the same\n");
    }
}
void longerString(char*name1, char*name2){
    int sizeName1 = strlen(name1);
    int sizeName2 = strlen(name2);

    if(sizeName1 == sizeName2) printf("the names is are the same\n");
    else if(sizeName1 > sizeName2) printf("The name %s is more longer", name1);
    else printf("The name %s is more longer\n", name2);
}
void concatenateString(char*name1, char*name2){
    char names[100];
    strncpy(names, name1, sizeof(names) - 1);
    names[sizeof(names) - 1] = '\0';
    strncat(names, name2, sizeof(names) - strlen(names) - 1);

    printf("The names in a single name is %s hello!!\n", names);
}
void mayusString(char*name1, char*name2){
    for(int i=0;name1[i] != '\0';i++){
        name1[i] = toupper(name1[i]);
    }
    for(int i=0;name2[i] != '\0';i++){
        name2[i] = toupper(name2[i]);
    }
    
    printf("\nHello %s", name1);
    printf(" and %s\n", name2);
}
