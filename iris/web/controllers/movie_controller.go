package controllers

import (
	"github.com/kataras/iris/mvc"
	"iris/repositories"
	"iris/service"
)

type MovieController struct{}

func (c *MovieController) Get() mvc.View {
	movieRepository := repositories.NewMovieManager()
	movieService := service.NewMovieServiceManager(movieRepository)
	MovieResult := movieService.ShowMovieName()
	return mvc.View{
		Name: "movie/index.html",
		Data: MovieResult,
	}
}
