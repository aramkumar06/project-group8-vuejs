package com.ssafy.model.service;

import java.util.List;

import com.ssafy.model.dto.Category;
import com.ssafy.model.dto.Youtuber;

public interface CategoryService {
	public List<Youtuber> search(int cano);
	public List<Category> searchAll();
}