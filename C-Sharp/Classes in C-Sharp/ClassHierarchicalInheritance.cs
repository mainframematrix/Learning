using System;

namespace ClassHierarchicalInheritance
{
    abstract class Human
    {
        string name;
        public Human(string humanName)
        {
            this.name = humanName;
        }
        public virtual void introduction()
        {
            Console.WriteLine($"Hi! My name is {name}.");
        }
    }

    class Student : Human
    {
        string schoolName;
        public Student(string HumanName, string nameSchool) : base(HumanName)
        {
            this.schoolName = nameSchool;
        }
        public override void introduction()
        {
            base.introduction();
            Console.WriteLine($"I study in {schoolName}");
        }
    }
    class Employee : Human
    {
        string officeName;
        public Employee(string name, string nameOffice) : base(name)
        {

            this.officeName = nameOffice;
        }
        public override void introduction()
        {
            base.introduction();
            Console.WriteLine($"I work in {officeName}");
        }
    }
    class HeirarchicalDemonstation
    {
        public void demonstate()
        {
            Console.WriteLine("Demonstation of Heirarchical Inheritance.\n");
            Student s1 = new Student("John Smith", "Roades Public School");
            Employee e1 = new Employee("Bill Smith", "GitHub");
            Console.WriteLine("\nStudent Introduction:");
            s1.introduction();
            Console.WriteLine("\nEmployee Introduction:");
            e1.introduction();
            Console.WriteLine("\n\n");
        }
    }
}