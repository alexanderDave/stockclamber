package Enterance;

import java.util.List;

import TestUnit.totalTest;
import TestUtil.PhoneUtil;
import TestUtil.conText;

public class test {

	public static void main(String[] args) throws InterruptedException {
		
		//1.获取当前所有连接的手机
		List<String> list = PhoneUtil.getPhoneserNum();
		//2.判断当前手机连接是否正常，如果正常的话先运行monkey吊起程序运行，然后开启线程统计性能指标
		if (!list.isEmpty()) {
			System.out.println("## Test main : get Phone info, start testing ##");
			for (String s:list) {
				//System.out.println(s);
				PhoneUtil.runCmd(conText.adb_s+s+conText.adb_monkey);//运行monkey
				
				Thread.sleep(5000);//等待5s 防止monkey开始执行时造成的参数不准						
				new totalTest(s);//开启线程对单台手机进行性能测试并获取指标		
			}			
		} else 
			System.out.println("##Test main:list of phone attached is empty , Please try again##");
	}

}
