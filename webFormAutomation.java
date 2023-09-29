package selenium;

import org.junit.After;
import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.interactions.Actions;
import org.openqa.selenium.support.ui.Select;

public class webFormAutomation {
	ChromeDriver driver = new ChromeDriver();
	@Before
	public void setUp() throws Exception {
        driver.get("https://www.selenium.dev/selenium/web/web-form.html");
        driver.manage().window().maximize();
	}

	@After
	public void tearDown() throws Exception {
		Thread.sleep(1000);
		driver.quit();
	}

	@Test
	public void test() throws InterruptedException {
		Thread.sleep(1000);
        
        //match title
        String title=driver.getTitle();
        System.out.println("Title is "+title);
        Assert.assertTrue(title.contains("Web form"));
        System.out.println("Test completed and page title is Verified");
        
        Thread.sleep(1000);
        
        //type text
        driver.findElement(By.name("my-text")).sendKeys("Hello");
        System.out.println("Text input made");
        
        Thread.sleep(1000);
        
        //type password
        driver.findElement(By.name("my-password")).sendKeys("1234");
        System.out.println("Password input made");
        
        //type text
        driver.findElement(By.name("my-textarea")).sendKeys("This is a webform automation");
        Thread.sleep(1000);
        
        //select from Dropoptions
        Select dropdown = new Select(driver.findElement(By.name("my-select")));  
        dropdown.selectByVisibleText("Two");  
        System.out.println("Dropdown option choosen");
        
        Thread.sleep(1000);
        
        //select from list
        
        WebElement element = driver.findElement(By.name("my-datalist"));
        element.sendKeys("New York");
        System.out.println("Dropdown datalist chosen");
        
        Thread.sleep(1000);
        
        //file upload
        driver.findElement(By.name("my-file")).sendKeys("C:\\college\\377\\text1.txt");
        System.out.println("File succesfully uploaded");        
        Thread.sleep(3000);
       
        //checkbox
        WebElement checkbox1=driver.findElement(By.id("my-check-1"));
        checkbox1.click();
        System.out.println("checked box unchecked");
        WebElement checkbox2=driver.findElement(By.id("my-check-2"));
        checkbox2.click();
        System.out.println("Default box checked");
        
        Thread.sleep(1000);
        
        //radio
        WebElement radio1=driver.findElement(By.id("my-radio-1"));
        radio1.click();
        System.out.println("checked radiobutton unchecked");
        WebElement radio2=driver.findElement(By.id("my-radio-2"));
        radio2.click();
        System.out.println("Default radiobutton checked");
        
        Thread.sleep(1000);
        
        //colorpicker
        WebElement color_picker=driver.findElement(By.name("my-colors"));
        String color_value = "#FF0000"; 
        color_picker.clear();  
        color_picker.sendKeys(color_value);
        System.out.println("Red color selected");
        
        Thread.sleep(1000);
        
        //datepicker
        WebElement calender=driver.findElement(By.name("my-date"));
        calender.click();
        for (int i = 0; i < 3; i++) {
            driver.findElement(By.xpath("/html/body/div/div[1]/table/thead/tr[2]/th[3]")).click();
        }
        WebElement desiredDate = driver.findElement(By.xpath("/html/body/div/div[1]/table/tbody/tr[6]/td[1]"));
        desiredDate.click();
        System.out.print("Date selected");
        
        Thread.sleep(1000);
        
        //rangepicker
        driver.findElement(By.xpath("/html/body/main/div/form/div/div[3]/label[3]/input"));
        WebElement slider=driver.findElement(By.name("my-range"));
        int sliderWidth = slider.getSize().getWidth();
        int percentage = -3;
        int targetPixel = (sliderWidth * percentage) / 10;
        Actions actions = new Actions(driver);
        actions.clickAndHold(slider).moveByOffset(targetPixel, 0).release().build().perform();
        System.out.println("Range selected");
        
        
        System.out.print("WebForm Successfully Automated");
	}

}
