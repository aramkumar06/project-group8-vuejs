package com.ssafy.model.service;

import java.util.List;

import com.ssafy.model.dto.User;
import com.ssafy.model.dto.Youtuber;

public interface UserService {
	public void insertUser(User user);
	public User search(String userID);
	public List<Youtuber> searchUserFavoriteYoutuber(String userID);
	public int searchUserExist(String userID);
}