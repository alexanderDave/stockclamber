package TestUtil;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;


public class FileUtil {
	//Tag for Log
	public static final String Tag = "## FileUtile :";
	
	public static InputStream openFile(String filepath){
		InputStream in = null;
		try {
			in = new FileInputStream(new File(filepath));
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return in;
	}
	
	public static void save2local(String in, String FileName){
		touchpath();
		createFile(FileName);
		FileOutputStream fos = null;
		try {
			fos = new FileOutputStream(conText.savePath+FileName);
			fos.write(in.getBytes());
			fos.flush();
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} finally {
			try {
				if (null != fos)
					fos.close();
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
		
	}
	
	private static void createFile(String fileName) {
		File file = new File(conText.savePath+fileName);
		if (!file.exists()) {
			try {
				file.createNewFile();
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
	}

	public static void touchpath(){
		File dir = new File(conText.savePath);
		if (!dir.exists()) {
			dir.mkdirs();
		}
	}
}
