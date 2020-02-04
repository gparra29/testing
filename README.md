# testing 1234
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

public class TestChrome {

    public static void main(String[] args) {

        //System.setProperty("webdriver.chrome.driver", "path of the exe file\\chromedriver.exe");

        // Initialize browser
        WebDriver driver = new ChromeDriver();

        // Open facebook
        driver.get("http://www.facebook.com");

        // Maximize browser
        driver.manage().window().maximize();

        // Close browser
        driver.quit();
    }
}
