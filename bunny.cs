using System;
using System.Collections.Generic;
using bunny;
namespace Mai{
  class bunnies{
    /// <summary>
    ///   The main entry point for the application
    /// </summary>
    [STAThread]
    public static void Main(string[] args)
    {
    //choose = new Bunny.Choose<string>();
    List<string> Colors = new List<string> {"White", "Black", "Brown", "Spotted"};
    List<string> sexes = new List<string> {"f", "m"};
    List<Bunny> bunlist = new List<Bunny> {};
    for(int i=0;i<=4;i++){
    string sex =  (string)Bunny.Choose<string>(sexes);
    Bunny bun = new Bunny(sex,Names.Init(sex),(string)Bunny.Choose(Colors));
    bunlist.Add(bun);}
    Console.WriteLine("{0},{1},{2}",bunlist[2].Sex,bunlist[2].Name,bunlist[2].Age);
    }
  }
}
namespace bunny{
  class Bunny{
    public string Sex {get; set;}
    public string Name {get; private set;}
    public int Age {get; set;}
    public string Color {get; private set;}
    //public Bunny[] Parents {get; set;}
    // /public static Bunny dumbBunny(){return Bunny("","","");}
    public Bunny(string sex, string name, string color){
      Sex = sex;
      Name = name;
      Age = 0;
      Color = color;
      //Parents = parents;
    }
    public override bool Equals(object obj){
    if (obj == null) return false;
    Bunny objAsPart = obj as Bunny;
    if (objAsPart == null) return false;
    else return Equals(objAsPart);
    }
    public bool Equals(Bunny other){
    if (other == null) return false;
    bool isEq = (this.Name.Equals(other.Name)) && (this.Sex.Equals(other.Sex)) && (this.Color.Equals(other.Color)) && (this.Age.Equals(other.Age));
    return isEq;
    }
    private void Rad(){
      Random rand = new Random();
      if (rand.Next(0,101) < 2)
      this.Sex = "X";
    }
    public static object Choose<T> (List<T> tlist){
      Random rand = new Random();
      return tlist[rand.Next(0,tlist.Count)];
    }
    public void Recreation( Bunny malbun, List<Bunny> bunlist){
      string f="f",F="F",m="m",M="M",X="X";
      string color = this.Color;
      Random rand = new Random();
      string sex = (rand.Next(0,101) > 50) ? f : m;
      Bunny child = new Bunny(sex , Names.Init(sex) , color );
      child.Rad();
      bunlist.Add(child);
    }
  public void kill(List<Bunny> bunlist){
    bunlist.Remove(this);
    return;
  }
  public void Tick(List<Bunny> bunlist){
    //choose = new Choose<Bunny>();
    this.Age += 1;
    if (bunlist.Count > 1000){
      for(int index=0;index<(int)(bunlist.Count/2);++index){
        bunlist.Remove((Bunny)Choose<Bunny>(bunlist));
      }}
    if (this.Sex != "X"){
      if (this.Age >= 2) this.Sex = this.Sex.ToUpper();
      if (this.Age > 10) this.kill(bunlist);
    }else{if (this.Age>50) this.kill(bunlist); else {Bunny mybun = (Bunny)Choose<Bunny>(bunlist); mybun.Sex="X";}}
    }
  }
  class Names{
    private static string[] Names_m = new string[] {"Thumper","Oreo","Oliver","Charlie","Coco","Pico","Jack","Peanut","Clover","Willow","Bailey"};
    private static string[] Names_f = new string[]  {"Daisy","Bella","Lola","Lily","Lucy","Thumper","Peanut","Clover","Molly","Bunbun","Pepper"};
    public static string Init(string sex){
      Random rand = new Random();
      if(sex=="m")
      return Names_m[rand.Next(0,Names_m.Length)];
      else
      return Names_f[rand.Next(0,Names_f.Length)];
    }
  }
}