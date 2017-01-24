import webapp2
import random

class Index(webapp2.RequestHandler):

    def getRandomMovie(self):

        movie_list = ["The Big Lebowski", "Big", "Tootsie", "The Matrix", "Fargo"]



        return random.choice(movie_list)

    def get(self):
        # choose a movie by invoking our new function
        movie = self.getRandomMovie()
        movie2= self.getRandomMovie()
        while movie == movie2:
            movie2= self.getRandomMovie()
        content = "<h1>Movie of the Day</h1>"
        content += "<p>" + movie + "</p>"

        content2 = "<h1>Tomorrow's movie </h1>"
        content2 += "<p>" + movie2 + "</p>"

        self.response.write(content)
        self.response.write(content2)

app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
