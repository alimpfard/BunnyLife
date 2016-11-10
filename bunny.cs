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
    int id=0;
    List<string> Colors = new List<string> {"White", "Black", "Brown", "Spotted"};
    List<string> sexes = new List<string> {"f", "m"};
    List<Bunny> bunlist = new List<Bunny> {};
    for(int i=0;i<=4;i++){
    string sex =  (string)Bunny.Choose<string>(sexes);
    Bunny bun = new Bunny(sex,Names.Init(sex),(string)Bunny.Choose(Colors),id);
    id++;
    bunlist.Add(bun);}
    while (true){
    List<Bunny> males = new List<Bunny> {};
    List<Bunny> females = new List<Bunny> {};
    foreach (Bunny bun in bunlist) {

      try
      {
              Console.Write("{0},{1},{2},{3}\t",bun.Sex,bun.Name,bun.Age,bun.Id);
              if (bun.Sex == "M") males.Add(bun);
              if (bun.Sex == "F") females.Add(bun);
              bun.Tick(bunlist);
      }
      catch(Exception e)
      {
      }
    }
    Console.WriteLine();
    foreach (Bunny mal in males) {
      foreach (Bunny fem in females) {
        try
        {
        fem.Recreation(mal,bunlist);
      }
      catch(Exception e){}
      }
    }
    }
  }
  }
}
namespace bunny{
  class Bunny{
    public string Sex {get; set;}
    public string Name {get; private set;}
    public int Age {get; set;}
    public string Color {get; private set;}
    public int Id {get; set;}
    private static readonly Random rand = new Random();
    //public Bunny[] Parents {get; set;}
    // /public static Bunny dumbBunny(){return Bunny("","","");}
    public Bunny(string sex, string name, string color, int id=0){
      Sex = sex;
      Name = name;
      Age = 0;
      Color = color;
      Id=id;
      //Parents = parents;
    }
    public override bool Equals(object obj){
    if (obj == null) return false;
    Bunny objAsPart = obj as Bunny;
    if (objAsPart == null) return false;
    else return Equals(objAsPart);
    }
    public override int GetHashCode()
{
    return this.Id;
}
    public bool Equals(Bunny other){
    if (other == null) return false;
    bool isEq = (this.Name.Equals(other.Name)) && (this.Sex.Equals(other.Sex)) && (this.Color.Equals(other.Color)) && (this.Age.Equals(other.Age));
    return isEq;
    }
    private void Rad(){
    //  Random rand = new Random();
      if (rand.Next(0,101) < 2)
      this.Sex = "X";
    }
    public static object Choose<T> (List<T> tlist){
      //Random rand = new Random();
      return tlist[rand.Next(0,tlist.Count)];
    }
    private static int ChooseIndex<T> (List<T> tlist){
      //Random rand = new Random();
      return rand.Next(0,tlist.Count);
    }
    public void Recreation( Bunny malbun, List<Bunny> bunlist){
      string f="f",F="F",m="m",M="M",X="X";
      string color = this.Color;
      //Random rand = new Random();
      string sex = (rand.Next(0,101) > 50) ? f : m;
      Bunny child = new Bunny(sex , Names.Init(sex) , color ,(this.Id+malbun.Id+1));
      child.Rad();
      bunlist.Add(child);
    }
  public void kill(List<Bunny> bunlist){
    bunlist.RemoveAt(bunlist.IndexOf(this));
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
    private static readonly Random rand = new Random();
    public static string Init(string sex){
      //Random rand = new Random();
      if(sex=="m")
      return Names_m[rand.Next(0,Names_m.Length)];
      else
      return Names_f[rand.Next(0,Names_f.Length)];
    }
  }
}
