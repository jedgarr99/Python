
import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.io.UnsupportedEncodingException;
import java.util.Scanner;

public class SumaNumeros {

    public static void main(String[] args) throws UnsupportedEncodingException {
        File file = new File("C:\\Users\\Edgar\\Desktop\\EDA Viernes\\datos.txt");
        
        try{
            Scanner lec = new Scanner(file);
            PrintWriter writer = new PrintWriter("salida");
            int k, a, b;
            
            k=lec.nextInt();          
            for(int i=0; i<k;i++){
                a=lec.nextInt();
                b=lec.nextInt();
                writer.println(a+b);
            }
            lec.close();
            writer.close();
        }
        catch(FileNotFoundException e) {
            e.printStackTrace();
        } 
    }
    
}
