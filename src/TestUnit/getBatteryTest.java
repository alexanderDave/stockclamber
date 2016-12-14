package TestUnit;

import java.text.SimpleDateFormat;
import java.util.Date;

import TestUtil.FileUtil;
import TestUtil.PhoneUtil;
import TestUtil.conText;

public class getBatteryTest extends Thread{
	//Tag for Log
	private static final String Tag = "## getBatteryTest :";
	private String devices = null;
	private int times = 10;
	private String result = null;
	private String bty_new = null, bty_old = null;
	
	public getBatteryTest(String s, int times) {
		this.devices = s;
		this.times = times;
		bty_new = conText.adb_s + devices + conText.batteryInfo_new + conText.pkgName_zm;
		bty_old = conText.adb_s + devices + conText.batteryInfo_old + conText.pkgName_zm;
	}
	
	@Override
	public void run() {
		System.out.println(Tag+"µÁ¡ø≤‚ ‘£∫");
		if (PhoneUtil.judge(devices)) 
			result = bty_old;
		else 
			result = bty_new;
				
		FileUtil.save2local(PhoneUtil.excuteCmd(result, ""),"getBatteryTest"+devices+"_"+(new SimpleDateFormat("yyyyMMddHHmmss")).format(new Date())+".txt");
	}
}
