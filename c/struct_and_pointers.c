#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<ctype.h>

struct Student{
    char name[50];
    int age;
    float grade;
};

void clearNewLine(char*);
void inputStudents(struct Student*);
void printStudent(struct Student*);
void nameToUpper(struct Student*);

int main(){
    int n;
    printf("How many students do you want to enter?: ");
    scanf("%d", &n);
    getchar();


    struct Student* students = malloc(n * sizeof(struct Student));

    if(students == NULL){
        printf("Memory allocation failed!!");
        return 1;
    }

    for(int i=0;i<n;i++){
        printf("\n--Student %d--\n", i+1);
        inputStudents(&students[i]);
    }


    for(int i=0;i<n;i++){
        nameToUpper(&students[i]);
    }


    for(int i=0;i<n;i++){
        printStudent(&students[i]);
    }

    free(students);
    students = NULL;

    return 0;
}
void clearNewLine(char*name){
    name[strcspn(name, "\n")] = '\0';
}
void inputStudents(struct Student*s){
    printf("Enter name: ");
    fgets(s->name, sizeof(s->name), stdin);
    clearNewLine(s->name);

    printf("Enter age: ");
    scanf("%d", &s->age);
    printf("Enter grade: ");
    scanf("%f", &s->grade);

    getchar();
}

void printStudent(struct Student*s){
    printf("Name: %s | age: %d | grade: %.2f\n", s->name,s->age,s->grade);
}

void nameToUpper(struct Student*s){
    for(int i=0;s->name[i] != '\0';i++){
        s->name[i] = toupper(s->name[i]);
    }
}
