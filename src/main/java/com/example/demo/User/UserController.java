package com.example.demo.User;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class UserController {

	@Autowired 
	UserDAO userDao;
	
	@GetMapping(value="/allUser")
	public List<User> findAllUser(){
		return userDao.findALL();
	}
}
