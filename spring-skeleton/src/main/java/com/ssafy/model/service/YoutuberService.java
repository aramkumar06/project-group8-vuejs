package com.ssafy.model.service;

import java.util.List;

import com.ssafy.model.dto.Youtuber;

public interface YoutuberService {
	public List<Youtuber> search(String name);
	public List<Youtuber> searchAll();
	public void insert(Youtuber youtuber);
}
