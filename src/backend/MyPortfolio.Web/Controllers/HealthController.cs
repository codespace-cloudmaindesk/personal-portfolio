using Microsoft.AspNetCore.Mvc;

namespace MyPortfolio.Web.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class HealthController : ControllerBase
    {
        [HttpGet]
        public IActionResult Get()
        {
            return Ok(new { status = "Healthy", message = "Backend is running and connected!" });
        }
    }
}
