package com.example.demo.User;

import java.util.ArrayList;
import java.util.List;

import org.springframework.stereotype.Component;

@Component
public class UserDAO {
	
	private static List<User> users=new ArrayList<User>();
		
		
		static {
			users.add(new User(222,"Tim","tim@gmail.com",6789));
			
			users.add(new User(333,"Sam","sam@gmail.com",4000));
			users.add(new User(444,"Ram","ram@gmail.com",3500));
			users.add(new User(555,"Kim","kim@gmail.com",4200));
			
		}
		
		public List<User> findALL(){
			return users;
		}


}
