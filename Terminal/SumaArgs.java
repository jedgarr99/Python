
import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.io.UnsupportedEncodingException;

public class SumaArgs {

    public static void main(String[] args) throws UnsupportedEncodingException {
        try{
            PrintWriter writer = new PrintWriter("salida3");
            int k, a, b;
            
            k=Integer.parseInt(args[0]);    
            for(int i=1; i<=k;i++){
                a=Integer.parseInt(args[2*i-1]);
                b=Integer.parseInt(args[2*i]);
                writer.println(a+b);
            }
            writer.close();
        }
        catch(FileNotFoundException e) {
            e.printStackTrace();
        } 
    }
    
}
