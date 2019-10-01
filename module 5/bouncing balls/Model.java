package bouncing_balls;

/**
 * The physics model.
 * 
 * The code has intentionally been kept as simple as possible, but if you wish, you can improve the design.
 * 
 * @author Simon Robillard and Dag Wedelin
 *
 */
class Model {

	double areaWidth, areaHeight;
	double cWall=3000;
	
	Ball [] balls;

	Model(double width, double height) {
		areaWidth = width;
		areaHeight = height;
		
		// Initialize the model with a few balls
		balls = new Ball[3];
		balls[0] = new Ball(width / 3, height * 0.9, 1.1, 1.1, 0.2,1);
		balls[1] = new Ball(2 * width / 3, height * 0.7, -0.4, 0.4, 0.3,4);
		balls[2] = new Ball(width / 5, height * 0.1, 0.1, 1.6, 0.4,2);
	}
	
	


	void step(double deltaT) {
	
		// calculate net force vector (fx,fy) for each ball by summing different forces from the environment
	
		double depth, depthX, depthY;

		for (Ball b : balls) {
		
			b.fx=0;
			b.fy=0;
			
			// walls provide opposite force
			
			if ((depth = b.radius-b.x) > 0) { // ball touches left side
				b.fx += cWall * depth;
			}
			if ((depth = b.x -(areaWidth-b.radius)) > 0) { // ball touches right side
				b.fx += cWall * (-depth);	
			}
			if ((depth = b.radius-b.y) > 0) { // ball touches lower side
				if (b.vy<=0) b.fy += cWall * depth;
				if (b.vy>0 ) b.fy += 0.9* cWall * depth; // trick: if upwards slightly lower force
			}
			if ((depth = b.y-(areaHeight-b.radius)) > 0) { // ball touches upper side
				b.fy += cWall * (-depth);
			}
			
			// gravity
			b.fy += b.mass * (-9.82);
			
			// collision
			for (Ball b2 : balls) {
			if (b2 != b) {  // collide only with other balls 
		
				// first create a unit vector (vector of length 1), in the direction of the force
				double deltaX = b.x-b2.x;
				double deltaY = b.y-b2.y;
				double dist=Math.sqrt(deltaX*deltaX + deltaY*deltaY);
				deltaX = deltaX/dist;
				deltaY = deltaY/dist;
		
				if ((depth = b.radius + b2.radius - dist) > 0) {
					b.fx +=  cWall * depth * deltaX;
					b.fy +=  cWall * depth * deltaY;
				}
			}
			}
		}
		
		for (Ball b : balls) {
		
			// forces ready, now update!
		
			// translate force into acceleration with Newtons law F=ma 
			b.ax = b.fx/b.mass;
			b.ay = b.fy/b.mass;
			
			// compute new velocity and position from the current acceleration and velocity of the ball
			b.vx = b.vx + b.ax * deltaT;
			b.vy = b.vy + b.ay * deltaT;
			b.x = b.x + b.vx * deltaT;
			b.y = b.y + b.vy * deltaT;
		}
		
		
	}
	
	
	
	
	/**
	 * Simple inner class describing balls.
	 */
	class Ball {
		
		Ball(double x, double y, double vx, double vy, double r,double m) {
			this.x = x;
			this.y = y;
			this.vx = vx;
			this.vy = vy;
			this.radius = r;
			this.mass = m;
		}

		/**
		 * Position, speed etc. of the ball.
		 */
		double x, y, vx, vy, ax, ay, radius, mass, fx,fy;
	}
}
