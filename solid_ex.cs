interface Movable
{
    Vector getPosition();
    Vector getVelocity();
    void setPosition(Vector newValue);
}

class Move
{
    public movable;
    public Move(Movable m)
    {
        movable = m;
    }
    public void Execute()
    {
        movable.setPosition(
            Vector.Plus(
                movable.getPosition(),
                movable.getVelocity()
            )
        );
    }
}         

class Ratable
{

}

class Rotate
{

}

interface UObject
{
    object getValue(string key);
    void setValue(string key,object newValue);
}

class MovableAdapter: Movable
{
    UObject Obj;
    public MovableAdapter(UObject o)
    {
        Obj = o;
    }
    Vector getPosition() 
    {
        return (Vector)Obj["position"];    
    }
    Vectot getVelosity()
    {
        return (Vector)Obj["velocity"];
    }
    void setPosition(Vector newValue) 
    {
         Obj["position"] = newValue;
    }
}

class SpaceShip: Movable, Ratable, Fireable, FuelBurnable
{
    private Vector position;
    private int velocityModule; 
    private int direction;
    private int angularVelocity;  
    private int burnLevel;
    private int burnVelocity;

    Vector getVector(){
        return position
    }
    Vector getPosition() {}
    void setPosition(Vector newValue) {}
}