/* USER CODE BEGIN Header */
/**
  ******************************************************************************
  * @file           : main.c
  * @brief          : Main program body
  ******************************************************************************
  * @attention
  *
  * Copyright (c) 2022 STMicroelectronics.  number = 0;
  * All rights reserved.
  *
  * This software is licensed under terms that can be found in the LICENSE file
  * in the root directory of this software component.
  * If no LICENSE file comes with this software, it is provided AS-IS.
  *
  ******************************************************************************
  */
/* USER CODE END Header */
/* Includes ------------------------------------------------------------------*/
#include "main.h"

/* Private includes ----------------------------------------------------------*/
/* USER CODE BEGIN Includes */
#include <stdio.h>
#include <stdbool.h>

/* USER CODE END Includes */

/* Private typedef -----------------------------------------------------------*/
/* USER CODE BEGIN PTD */

/* USER CODE END PTD */

/* Private define ------------------------------------------------------------*/
/* USER CODE BEGIN PD */
uint16_t ADCDMABuff[3];
/* USER CODE END PD */

/* Private macro -------------------------------------------------------------*/
/* USER CODE BEGIN PM */
#define ARM_CM_DEMCR (*(uint32_t *)0xE000EDFC)
#define ARM_CM_DWT_CTRL (*(uint32_t *)0xE0001000)
#define ARM_CM_DWT_CYCCNT (*(uint32_t *)0xE0001004)
#define CPU_CLOCK_FREQ ((double)100000000)

#define BUFFER_LEN (3000)
uint32_t BufferT[BUFFER_LEN];
uint16_t BufferAD[BUFFER_LEN];
/* USER CODE END PM */

/* Private variables ---------------------------------------------------------*/
ADC_HandleTypeDef hadc1;
DMA_HandleTypeDef hdma_adc1;

SPI_HandleTypeDef hspi1;

TIM_HandleTypeDef htim1;
TIM_HandleTypeDef htim2;
TIM_HandleTypeDef htim4;

UART_HandleTypeDef huart2;

/* USER CODE BEGIN PV */
static unsigned number = 0;
static unsigned TimerCnt = 0;
static unsigned ADCRes = 0;
uint32_t time_1;
uint32_t time_2;
static unsigned WYNIK_ADC = 0;
static unsigned current_index = 0;


static int8_t x;
static int8_t y;
static int8_t z;


static unsigned SPI_counter = 0;

uint16_t SPITx[10];
uint16_t SPIRx[10];
uint8_t SPIRead( uint8_t Address ) {
     SPITx[0] = (0x80 | Address) << 8;
     HAL_GPIO_WritePin(GPIOA, SPI_NSS_Pin, GPIO_PIN_RESET);
     HAL_SPI_TransmitReceive(&hspi1, SPITx, SPIRx, 1, 100);
     HAL_GPIO_WritePin(GPIOA, SPI_NSS_Pin, GPIO_PIN_SET);
 return( (uint8_t)(SPIRx[0] & 0xFF) );
}
void SPIWrite( uint8_t AddressAndAtributes, uint8_t Data ) {
     SPITx[0] = (AddressAndAtributes << 8) + Data;
     HAL_GPIO_WritePin(GPIOA, SPI_NSS_Pin, GPIO_PIN_RESET);
     HAL_SPI_TransmitReceive(&hspi1, SPITx, SPIRx, 1, 100);
     HAL_GPIO_WritePin(GPIOA, SPI_NSS_Pin, GPIO_PIN_SET);
}


void set_flags(){
    SPIWrite(0x20,0b11000111); // CTRL_REG1 – DR, PD, Zen, Yen i Xen
    SPIWrite(0x21,0b00000000); // CTRL_REG2 – BOOT.
    SPIWrite(0x22,0b10000111);// CTRL_REG3 – IHL, I1CFG2, I1CFG1 i I1CFG0.
    SPIWrite(0x38,0b00101010);  // CLCK_CFG
    SPIWrite(0x3b,0b00110011);  // click_thsy_x
    SPIWrite(0x3c,0b00001111);
    SPIWrite(0x3d,0x88);
    SPIWrite(0x3e,0x22);
    SPIWrite(0x3f,0xff);
}
/* USER CODE END PV */

/* Private function prototypes -----------------------------------------------*/
void SystemClock_Config(void);
static void MX_GPIO_Init(void);
static void MX_DMA_Init(void);
static void MX_USART2_UART_Init(void);
static void MX_TIM1_Init(void);
static void MX_ADC1_Init(void);
static void MX_TIM4_Init(void);
static void MX_TIM2_Init(void);
static void MX_SPI1_Init(void);
/* USER CODE BEGIN PFP */
void chose_screen_and_number(int,int);
void DisplayNumber(int);
void reset_screen();
/* USER CODE END PFP */

/* Private user code ---------------------------------------------------------*/
/* USER CODE BEGIN 0 */
void reset_screen () {
    HAL_GPIO_WritePin(GPIOC, S7Com1_Pin, GPIO_PIN_SET);
    HAL_GPIO_WritePin(GPIOC, S7Com2_Pin, GPIO_PIN_SET);
    HAL_GPIO_WritePin(GPIOC, S7Com3_Pin, GPIO_PIN_SET);
    HAL_GPIO_WritePin(GPIOC, S7Com4_Pin, GPIO_PIN_SET);
}

void chose_screen_and_number (int screen, int number) {
    //Wybór ekranu
    switch (screen) {
    	case 0:
			HAL_GPIO_WritePin(GPIOC, S7Com1_Pin, GPIO_PIN_RESET);
			HAL_GPIO_WritePin(GPIOC, S7Com2_Pin, GPIO_PIN_RESET);
			HAL_GPIO_WritePin(GPIOC, S7Com3_Pin, GPIO_PIN_RESET);
			HAL_GPIO_WritePin(GPIOC, S7Com4_Pin, GPIO_PIN_RESET);
        break;
        case 1:
            HAL_GPIO_WritePin(GPIOC, S7Com1_Pin, GPIO_PIN_RESET);
            HAL_GPIO_WritePin(GPIOC, S7Com2_Pin, GPIO_PIN_SET);
            HAL_GPIO_WritePin(GPIOC, S7Com3_Pin, GPIO_PIN_SET);
            HAL_GPIO_WritePin(GPIOC, S7Com4_Pin, GPIO_PIN_SET);
            break;
        case 2:
            HAL_GPIO_WritePin(GPIOC, S7Com1_Pin, GPIO_PIN_SET);
            HAL_GPIO_WritePin(GPIOC, S7Com2_Pin, GPIO_PIN_RESET);
            HAL_GPIO_WritePin(GPIOC, S7Com3_Pin, GPIO_PIN_SET);
            HAL_GPIO_WritePin(GPIOC, S7Com4_Pin, GPIO_PIN_SET);
            break;
        case 3:
            HAL_GPIO_WritePin(GPIOC, S7Com1_Pin, GPIO_PIN_SET);
            HAL_GPIO_WritePin(GPIOC, S7Com2_Pin, GPIO_PIN_SET);
            HAL_GPIO_WritePin(GPIOC, S7Com3_Pin, GPIO_PIN_RESET);
            HAL_GPIO_WritePin(GPIOC, S7Com4_Pin, GPIO_PIN_SET);
            break;
        case 4:
            HAL_GPIO_WritePin(GPIOC, S7Com1_Pin, GPIO_PIN_SET);
            HAL_GPIO_WritePin(GPIOC, S7Com2_Pin, GPIO_PIN_SET);
            HAL_GPIO_WritePin(GPIOC, S7Com3_Pin, GPIO_PIN_SET);
            HAL_GPIO_WritePin(GPIOC, S7Com4_Pin, GPIO_PIN_RESET);
            break;

        default:
            reset_screen();
    }
    //Wybór liczby którą chcemy wypisać na ekranie
    switch (number) {
        case 0:
            HAL_GPIO_WritePin(GPIOC, S7A_Pin, GPIO_PIN_SET);
            HAL_GPIO_WritePin(GPIOC, S7B_Pin, GPIO_PIN_SET);
            HAL_GPIO_WritePin(GPIOC, S7C_Pin, GPIO_PIN_SET);
            HAL_GPIO_WritePin(GPIOC, S7D_Pin, GPIO_PIN_SET);
            HAL_GPIO_WritePin(GPIOC, S7E_Pin, GPIO_PIN_SET);
            HAL_GPIO_WritePin(GPIOC, S7F_Pin, GPIO_PIN_SET);
            HAL_GPIO_WritePin(GPIOC, S7G_Pin, GPIO_PIN_RESET);
            break;
        case 1:
            HAL_GPIO_WritePin(GPIOC, S7A_Pin, GPIO_PIN_RESET);
            HAL_GPIO_WritePin(GPIOC, S7B_Pin, GPIO_PIN_SET);
            HAL_GPIO_WritePin(GPIOC, S7C_Pin, GPIO_PIN_SET);
            HAL_GPIO_WritePin(GPIOC, S7D_Pin, GPIO_PIN_RESET);
            HAL_GPIO_WritePin(GPIOC, S7E_Pin, GPIO_PIN_RESET);
            HAL_GPIO_WritePin(GPIOC, S7F_Pin, GPIO_PIN_RESET);
            HAL_GPIO_WritePin(GPIOC, S7G_Pin, GPIO_PIN_RESET);
            break;
        case 2:
            HAL_GPIO_WritePin(GPIOC, S7A_Pin, GPIO_PIN_SET);
            HAL_GPIO_WritePin(GPIOC, S7B_Pin, GPIO_PIN_SET);
            HAL_GPIO_WritePin(GPIOC, S7C_Pin, GPIO_PIN_RESET);
            HAL_GPIO_WritePin(GPIOC, S7D_Pin, GPIO_PIN_SET);
            HAL_GPIO_WritePin(GPIOC, S7E_Pin, GPIO_PIN_SET);
            HAL_GPIO_WritePin(GPIOC, S7F_Pin, GPIO_PIN_RESET);
            HAL_GPIO_WritePin(GPIOC, S7G_Pin, GPIO_PIN_SET);
            break;
        case 3:
            HAL_GPIO_WritePin(GPIOC, S7A_Pin, GPIO_PIN_SET);
            HAL_GPIO_WritePin(GPIOC, S7B_Pin, GPIO_PIN_SET);
            HAL_GPIO_WritePin(GPIOC, S7C_Pin, GPIO_PIN_SET);
            HAL_GPIO_WritePin(GPIOC, S7D_Pin, GPIO_PIN_SET);
            HAL_GPIO_WritePin(GPIOC, S7E_Pin, GPIO_PIN_RESET);
            HAL_GPIO_WritePin(GPIOC, S7F_Pin, GPIO_PIN_RESET);
            HAL_GPIO_WritePin(GPIOC, S7G_Pin, GPIO_PIN_SET);
            break;
        case 4:
            HAL_GPIO_WritePin(GPIOC, S7A_Pin, GPIO_PIN_RESET);
            HAL_GPIO_WritePin(GPIOC, S7B_Pin, GPIO_PIN_SET);
            HAL_GPIO_WritePin(GPIOC, S7C_Pin, GPIO_PIN_SET);
            HAL_GPIO_WritePin(GPIOC, S7D_Pin, GPIO_PIN_RESET);
            HAL_GPIO_WritePin(GPIOC, S7E_Pin, GPIO_PIN_RESET);
            HAL_GPIO_WritePin(GPIOC, S7F_Pin, GPIO_PIN_SET);
            HAL_GPIO_WritePin(GPIOC, S7G_Pin, GPIO_PIN_SET);
            break;
        case 5:
            HAL_GPIO_WritePin(GPIOC, S7A_Pin, GPIO_PIN_SET);
            HAL_GPIO_WritePin(GPIOC, S7B_Pin, GPIO_PIN_RESET);
            HAL_GPIO_WritePin(GPIOC, S7C_Pin, GPIO_PIN_SET);
            HAL_GPIO_WritePin(GPIOC, S7D_Pin, GPIO_PIN_SET);
            HAL_GPIO_WritePin(GPIOC, S7E_Pin, GPIO_PIN_RESET);
            HAL_GPIO_WritePin(GPIOC, S7F_Pin, GPIO_PIN_SET);
            HAL_GPIO_WritePin(GPIOC, S7G_Pin, GPIO_PIN_SET);
            break;
        case 6:
            HAL_GPIO_WritePin(GPIOC, S7A_Pin, GPIO_PIN_SET);
            HAL_GPIO_WritePin(GPIOC, S7B_Pin, GPIO_PIN_RESET);
            HAL_GPIO_WritePin(GPIOC, S7C_Pin, GPIO_PIN_SET);
            HAL_GPIO_WritePin(GPIOC, S7D_Pin, GPIO_PIN_SET);
            HAL_GPIO_WritePin(GPIOC, S7E_Pin, GPIO_PIN_SET);
            HAL_GPIO_WritePin(GPIOC, S7F_Pin, GPIO_PIN_SET);
            HAL_GPIO_WritePin(GPIOC, S7G_Pin, GPIO_PIN_SET);
            break;
        case 7:
            HAL_GPIO_WritePin(GPIOC, S7A_Pin, GPIO_PIN_SET);
            HAL_GPIO_WritePin(GPIOC, S7B_Pin, GPIO_PIN_SET);
            HAL_GPIO_WritePin(GPIOC, S7C_Pin, GPIO_PIN_SET);
            HAL_GPIO_WritePin(GPIOC, S7D_Pin, GPIO_PIN_RESET);
            HAL_GPIO_WritePin(GPIOC, S7E_Pin, GPIO_PIN_RESET);
            HAL_GPIO_WritePin(GPIOC, S7F_Pin, GPIO_PIN_RESET);
            HAL_GPIO_WritePin(GPIOC, S7G_Pin, GPIO_PIN_RESET);
            break;
        case 8:
            HAL_GPIO_WritePin(GPIOC, S7A_Pin, GPIO_PIN_SET);
            HAL_GPIO_WritePin(GPIOC, S7B_Pin, GPIO_PIN_SET);
            HAL_GPIO_WritePin(GPIOC, S7C_Pin, GPIO_PIN_SET);
            HAL_GPIO_WritePin(GPIOC, S7D_Pin, GPIO_PIN_SET);
            HAL_GPIO_WritePin(GPIOC, S7E_Pin, GPIO_PIN_SET);
            HAL_GPIO_WritePin(GPIOC, S7F_Pin, GPIO_PIN_SET);
            HAL_GPIO_WritePin(GPIOC, S7G_Pin, GPIO_PIN_SET);
            break;
        case 9:
            HAL_GPIO_WritePin(GPIOC, S7A_Pin, GPIO_PIN_SET);
            HAL_GPIO_WritePin(GPIOC, S7B_Pin, GPIO_PIN_SET);
            HAL_GPIO_WritePin(GPIOC, S7C_Pin, GPIO_PIN_SET);
            HAL_GPIO_WritePin(GPIOC, S7D_Pin, GPIO_PIN_SET);
            HAL_GPIO_WritePin(GPIOC, S7E_Pin, GPIO_PIN_RESET);
            HAL_GPIO_WritePin(GPIOC, S7F_Pin, GPIO_PIN_SET);
            HAL_GPIO_WritePin(GPIOC, S7G_Pin, GPIO_PIN_SET);
            break;
        default:
        	HAL_GPIO_WritePin(GPIOC, S7A_Pin, GPIO_PIN_RESET);
        	HAL_GPIO_WritePin(GPIOC, S7B_Pin, GPIO_PIN_RESET);
        	HAL_GPIO_WritePin(GPIOC, S7C_Pin, GPIO_PIN_RESET);
        	HAL_GPIO_WritePin(GPIOC, S7D_Pin, GPIO_PIN_RESET);
        	HAL_GPIO_WritePin(GPIOC, S7E_Pin, GPIO_PIN_RESET);
        	HAL_GPIO_WritePin(GPIOC, S7F_Pin, GPIO_PIN_RESET);
        	HAL_GPIO_WritePin(GPIOC, S7G_Pin, GPIO_PIN_RESET);
        	break;
    }
    HAL_Delay(1);
    reset_screen();
}


void DisplayNumber(int number)
{
    int numbers[4] = {-1,-1,-1,-1};
    for (int i = 0; i<4; i++){
        numbers[i] = number % 10;
        number = number / 10;
    }
    int n4 = numbers[0];
    int n3 = numbers[1];
    int n2 = numbers[2];
    int n1 = numbers[3];

    reset_screen();
    chose_screen_and_number(1, n1);
    reset_screen();
    chose_screen_and_number(2, n2);
    reset_screen();
    chose_screen_and_number(3, n3);
    reset_screen();
    chose_screen_and_number(4, n4);
}

//Przerwania od przycisków:
void HAL_GPIO_EXTI_Callback(uint16_t GPIO_Pin){
    if( GPIO_Pin == Button1_Pin) {
        if (time_1 + 100 < HAL_GetTick()){
            number++;
            time_1 = HAL_GetTick();
        }

    }
    if( GPIO_Pin == Button2_Pin) {
        if (time_2 + 100 < HAL_GetTick() && number > 0){
            number--;
            time_2 = HAL_GetTick();
        }
    }
    if(GPIO_Pin == ClickInterrupt_Pin) {
        SPI_counter++;

        // Wyświetlanie w cutecom
        printf("licznik: %d\n ", SPI_counter);
        printf("x: %3d ",x);
        printf("y: %3d ",y);
        printf("z: %3d\n",z);
    }
}

int __io_putchar(int ch) {
    HAL_UART_Transmit(&huart2, (uint8_t *)&ch, 1, 0xFFFF);
    return ch;
}

int getchar(void) {
    uint8_t value;
    if( __HAL_UART_GET_FLAG(&huart2, UART_FLAG_RXNE) != SET )
        return( -1 );
    if (__HAL_UART_GET_FLAG(&huart2, UART_FLAG_RXNE) == SET)
        HAL_UART_Receive(&huart2, &value, 1, 100);
    __io_putchar( value );
    return ((int) value);
}


void InterruptDisplay(int TimerCnt){
	DisplayNumber(TimerCnt);
}

void ADC_RES_Display(int WYNIK_ADC){
	DisplayNumber(WYNIK_ADC);
}


// procedura przerwania timer'a:
void HAL_TIM_PeriodElapsedCallback(TIM_HandleTypeDef *htim) {
	if( htim == &htim1 ){
		if (TimerCnt == 9999){
			TimerCnt = 0;
		}
		TimerCnt++;
	}
	if( htim == &htim4 ) {

        //Włączone przy przetwarzaniu:
//		HAL_ADC_Start(&hadc1);
//		HAL_ADC_PollForConversion(&hadc1, HAL_MAX_DELAY);
//		ADCRes = HAL_ADC_GetValue(&hadc1); // 0-4095 == 0-3.3V
//		ADCRes = (uint16_t)(3.3 * (double)ADCRes / 4.095); // [mV]

        //Włączone w zadaniu 7:
        x = (int8_t) SPIRead(0x29);
        y = (int8_t) SPIRead(0x2B);
        z = (int8_t) SPIRead(0x2D);
	}
}

//void HAL_ADC_ConvCpltCallback(ADC_HandleTypeDef* hadc) {
//	WYNIK_ADC = HAL_ADC_GetValue(&hadc1);
//}

void HAL_ADC_ConvCpltCallback(ADC_HandleTypeDef* hadc) {
	//int dif = 1e6*((double)Stop-(double)Start)/CPU_CLOCK_FREQ;
	ADCRes = HAL_ADC_GetValue(&hadc1);
	ADCRes = (3.3 * (double)ADCRes)/4.095;
	if (BUFFER_LEN > current_index){
		BufferAD[current_index] = ADCRes;
		BufferT[current_index] = ARM_CM_DWT_CYCCNT;
		current_index++;
	}
}

/* USER CODE END 0 */

/**
  * @brief  The application entry point.
  * @retval int
  */
int main(void)
{
  /* USER CODE BEGIN 1 */




  /* USER CODE END 1 */

  /* MCU Configuration--------------------------------------------------------*/

  /* Reset of all peripherals, Initializes the Flash interface and the Systick. */
  HAL_Init();

  /* USER CODE BEGIN Init */
  if (ARM_CM_DWT_CTRL != 0) { // See if DWT is available
	  ARM_CM_DEMCR |= 1 << 24; // Set bit 24
	  ARM_CM_DWT_CYCCNT = 0;
	  ARM_CM_DWT_CTRL |= 1 << 0; // Set bit 0
  }
  /* USER CODE END Init */

  /* Configure the system clock */
  SystemClock_Config();

  /* USER CODE BEGIN SysInit */

  /* USER CODE END SysInit */

  /* Initialize all configured peripherals */
  MX_GPIO_Init();
  MX_DMA_Init();
  MX_USART2_UART_Init();
  MX_TIM1_Init();
  MX_ADC1_Init();
  MX_TIM4_Init();
  MX_TIM2_Init();
  MX_SPI1_Init();
  /* USER CODE BEGIN 2 */
//  time_1 = HAL_GetTick();
//  time_2 = HAL_GetTick();

//  HAL_TIM_Base_Start_IT(&htim1);


  HAL_TIM_Base_Start_IT(&htim4);
//  HAL_ADC_Start(&hadc1);

  //Jak nie zadziała to zablokować zegar 2
  HAL_TIM_Base_Start(&htim2);
//  HAL_ADC_Start_IT(&hadc1);

  HAL_ADC_Start_DMA(&hadc1, (uint32_t *)ADCDMABuff, 3);

  set_flags();
  /* USER CODE END 2 */

  /* Infinite loop */
  /* USER CODE BEGIN WHILE */
  while (1)
  {
    /* USER CODE END WHILE */

    /* USER CODE BEGIN 3 */

    //Zadanie 2 wyświetlanie cyfr
    //Korzystam z funkcji DisplayNumber();, chose_screen_and_number (int screen, int number);, reset_screen ();
//    DisplayNumber(1234);

    //Zadanie 3 Przerwania od przycisków. Button_1 inkrementuje licznik, Button_2 dekrementuje licznik,
    //zdefiniować zmienną number jako static unsigned number = 0; Napisać funkcje :
    //void HAL_GPIO_EXTI_Callback(uint16_t GPIO_Pin) - wszystkie przerwania od przycisków
    //__io_putchar(int ch)
    // getchar(void)
    //Wywołanie na płytce:
//    DisplayNumber(number);
    //Wywołanie w Cutecom:
//    printf("%d", number);


    //Zadanie 4 Przerwania zegarowe. Odczyt i prezentacja wyniku konwersji A/C.
    //napisać funckję HAL_TIM_PeriodElapsedCallback - wszystkie przerwania od zegarów
    //Wykonać iniclalizację zegara 1 w USER CODE BEGIN 2
//    DisplaNumber(TimerCnt);
    //Wykonać iniclalizację zegara 4 w USER CODE BEGIN 2
    // Napisać w funckji HAL_TIM_PeriodElapsedCallback:
//    HAL_ADC_Start(&hadc1);
//    HAL_ADC_PollForConversion(&hadc1, HAL_MAX_DELAY);
//    ADCRes = HAL_ADC_GetValue(&hadc1); // 0-4095 == 0-3.3V
//    ADCRes = (uint16_t)(3.3 * (double)ADCRes / 4.095); // [mV]
//    HAL_Delay(100);


    //Laboratorium 5. Akwizycja danych z przetwornika A/C za pomocą przerwania.
    //Skonfigurować i zainicjować zegar 4 w USER CODE BEGIN 2
    //Piszemy lepszą obługę przerwań - moja aktualna funkcja HAL_TIM_PeriodElapsedCallback
    //Wywołanie do lab5 - druga część
    // Napisać funkcję HAL_ADC_ConvCpltCallback, zdefiniować potrzebne zmienne
    //Wywołanie:
//      if (current_index == 3000){
//          for (int i = 0; i < 3000; i++){
//              printf("BufferAD[%d] = %.1d\n", i, BufferAD[i]);
//              //printf("BufferT[%d] = %.1d\n", i, BufferT[i]);
//          }
//      }


    //Laboratorium 6. Akwizycja danych z przetwornika A/C kanałem DMA. Przerwanie od A/C wyzwalane poziomem.
    //Konfiguracja zgodnie ze skryptem
    //Zdefioniowanie tablicy w USER CODE BEGIN PD
    //Zainicjowanie pracy w  USER CODE BEGIN 2
    //Można też dodać funkcję HAL_ADC_LevelOutOfWindowCallback
    //Działanie programu do lab 6 - wyświetlanie danych:
//    float ADCDMABuff_scaled[3];
//    float volt = 1.21 * 4096 / ADCDMABuff[2];
//
//    ADCDMABuff_scaled[1] = volt * ADCDMABuff[1] / 4096;
//    ADCDMABuff_scaled[0] = volt * ADCDMABuff[0] / 4096;
//    ADCDMABuff_scaled[1] = ((ADCDMABuff_scaled[1] - 0.76f) / 0.0025f) + 25;
//    ADCDMABuff_scaled[2] = volt;
//
//    printf("%f [V]        ", ADCDMABuff_scaled[0]);
//    printf("%f [C]   ", ADCDMABuff_scaled[1]);
//    printf("%f [V] ", ADCDMABuff_scaled[2]);
//    printf("\n");
//
//    DisplayNumber(ADCDMABuff_scaled[1]);


    //Odczyt i prezentacja danych z MEMS. Obsługa SPI.
    //Konfiguracja
    //Sekwencja odczytu/zapisu po magistrali SPI, napisanie poniższych zmiennych:
    //uint16_t SPITx[10];
    //uint16_t SPIRx[10];
    //uint8_t SPIRead

    // Wyświetlanie liczby 7 na płytce i  na cutecom
//    printf("%d", SPIRead(0x20));
//    DisplayNumber(SPIRead(0x20));

    //Napisać funkcję set_flags() i  wywołać ją w USER CODE BEGIN 2
    //Zdefioniować zmienne:
    //static int8_t x;
    //static int8_t y;
    //static int8_t z;
    //Zmodyfikować funkcję HAL_TIM_PeriodElapsedCallback
    // Początek lab7 wyświetlanie bez funkcji przerwania
//    printf("x: %3d ", x);
//    printf("y: %3d ", y);
//    printf("z: %3d\n ", z);



    // Wyświetlanie x,y,z za pomocą funckji przerwania
    //Zakomentować powyższy kod do wyświetlanie bez funkcji przerwania
    //napisać zmienną SPI_counter
    //Zmodyfikować - dopisać ostatniego ifa w funkcji HAL_GPIO_EXTI_Callback
    //Wyświeltanie podwójnego tapnięcia:
//    DisplayNumber(SPI_counter);

  }
  /* USER CODE END 3 */
}

/**
  * @brief System Clock Configuration
  * @retval None
  */
void SystemClock_Config(void)
{
  RCC_OscInitTypeDef RCC_OscInitStruct = {0};
  RCC_ClkInitTypeDef RCC_ClkInitStruct = {0};

  /** Configure the main internal regulator output voltage
  */
  __HAL_RCC_PWR_CLK_ENABLE();
  __HAL_PWR_VOLTAGESCALING_CONFIG(PWR_REGULATOR_VOLTAGE_SCALE1);

  /** Initializes the RCC Oscillators according to the specified parameters
  * in the RCC_OscInitTypeDef structure.
  */
  RCC_OscInitStruct.OscillatorType = RCC_OSCILLATORTYPE_HSE;
  RCC_OscInitStruct.HSEState = RCC_HSE_BYPASS;
  RCC_OscInitStruct.PLL.PLLState = RCC_PLL_ON;
  RCC_OscInitStruct.PLL.PLLSource = RCC_PLLSOURCE_HSE;
  RCC_OscInitStruct.PLL.PLLM = 8;
  RCC_OscInitStruct.PLL.PLLN = 200;
  RCC_OscInitStruct.PLL.PLLP = RCC_PLLP_DIV2;
  RCC_OscInitStruct.PLL.PLLQ = 4;
  if (HAL_RCC_OscConfig(&RCC_OscInitStruct) != HAL_OK)
  {
    Error_Handler();
  }

  /** Initializes the CPU, AHB and APB buses clocks
  */
  RCC_ClkInitStruct.ClockType = RCC_CLOCKTYPE_HCLK|RCC_CLOCKTYPE_SYSCLK
                              |RCC_CLOCKTYPE_PCLK1|RCC_CLOCKTYPE_PCLK2;
  RCC_ClkInitStruct.SYSCLKSource = RCC_SYSCLKSOURCE_PLLCLK;
  RCC_ClkInitStruct.AHBCLKDivider = RCC_SYSCLK_DIV1;
  RCC_ClkInitStruct.APB1CLKDivider = RCC_HCLK_DIV2;
  RCC_ClkInitStruct.APB2CLKDivider = RCC_HCLK_DIV1;

  if (HAL_RCC_ClockConfig(&RCC_ClkInitStruct, FLASH_LATENCY_3) != HAL_OK)
  {
    Error_Handler();
  }
}

/**
  * @brief ADC1 Initialization Function
  * @param None
  * @retval None
  */
static void MX_ADC1_Init(void)
{

  /* USER CODE BEGIN ADC1_Init 0 */

  /* USER CODE END ADC1_Init 0 */

  ADC_AnalogWDGConfTypeDef AnalogWDGConfig = {0};
  ADC_ChannelConfTypeDef sConfig = {0};

  /* USER CODE BEGIN ADC1_Init 1 */

  /* USER CODE END ADC1_Init 1 */

  /** Configure the global features of the ADC (Clock, Resolution, Data Alignment and number of conversion)
  */
  hadc1.Instance = ADC1;
  hadc1.Init.ClockPrescaler = ADC_CLOCK_SYNC_PCLK_DIV4;
  hadc1.Init.Resolution = ADC_RESOLUTION_12B;
  hadc1.Init.ScanConvMode = ENABLE;
  hadc1.Init.ContinuousConvMode = DISABLE;
  hadc1.Init.DiscontinuousConvMode = DISABLE;
  hadc1.Init.ExternalTrigConvEdge = ADC_EXTERNALTRIGCONVEDGE_RISING;
  hadc1.Init.ExternalTrigConv = ADC_EXTERNALTRIGCONV_T2_TRGO;
  hadc1.Init.DataAlign = ADC_DATAALIGN_RIGHT;
  hadc1.Init.NbrOfConversion = 3;
  hadc1.Init.DMAContinuousRequests = ENABLE;
  hadc1.Init.EOCSelection = ADC_EOC_SINGLE_CONV;
  if (HAL_ADC_Init(&hadc1) != HAL_OK)
  {
    Error_Handler();
  }

  /** Configure the analog watchdog
  */
  AnalogWDGConfig.WatchdogMode = ADC_ANALOGWATCHDOG_SINGLE_REG;
  AnalogWDGConfig.HighThreshold = 2000;
  AnalogWDGConfig.LowThreshold = 0;
  AnalogWDGConfig.Channel = ADC_CHANNEL_1;
  AnalogWDGConfig.ITMode = ENABLE;
  if (HAL_ADC_AnalogWDGConfig(&hadc1, &AnalogWDGConfig) != HAL_OK)
  {
    Error_Handler();
  }

  /** Configure for the selected ADC regular channel its corresponding rank in the sequencer and its sample time.
  */
  sConfig.Channel = ADC_CHANNEL_1;
  sConfig.Rank = 1;
  sConfig.SamplingTime = ADC_SAMPLETIME_480CYCLES;
  if (HAL_ADC_ConfigChannel(&hadc1, &sConfig) != HAL_OK)
  {
    Error_Handler();
  }

  /** Configure for the selected ADC regular channel its corresponding rank in the sequencer and its sample time.
  */
  sConfig.Channel = ADC_CHANNEL_TEMPSENSOR;
  sConfig.Rank = 2;
  if (HAL_ADC_ConfigChannel(&hadc1, &sConfig) != HAL_OK)
  {
    Error_Handler();
  }

  /** Configure for the selected ADC regular channel its corresponding rank in the sequencer and its sample time.
  */
  sConfig.Channel = ADC_CHANNEL_VREFINT;
  sConfig.Rank = 3;
  if (HAL_ADC_ConfigChannel(&hadc1, &sConfig) != HAL_OK)
  {
    Error_Handler();
  }
  /* USER CODE BEGIN ADC1_Init 2 */

  /* USER CODE END ADC1_Init 2 */

}

/**
  * @brief SPI1 Initialization Function
  * @param None
  * @retval None
  */
static void MX_SPI1_Init(void)
{

  /* USER CODE BEGIN SPI1_Init 0 */

  /* USER CODE END SPI1_Init 0 */

  /* USER CODE BEGIN SPI1_Init 1 */

  /* USER CODE END SPI1_Init 1 */
  /* SPI1 parameter configuration*/
  hspi1.Instance = SPI1;
  hspi1.Init.Mode = SPI_MODE_MASTER;
  hspi1.Init.Direction = SPI_DIRECTION_2LINES;
  hspi1.Init.DataSize = SPI_DATASIZE_16BIT;
  hspi1.Init.CLKPolarity = SPI_POLARITY_LOW;
  hspi1.Init.CLKPhase = SPI_PHASE_1EDGE;
  hspi1.Init.NSS = SPI_NSS_SOFT;
  hspi1.Init.BaudRatePrescaler = SPI_BAUDRATEPRESCALER_16;
  hspi1.Init.FirstBit = SPI_FIRSTBIT_MSB;
  hspi1.Init.TIMode = SPI_TIMODE_DISABLE;
  hspi1.Init.CRCCalculation = SPI_CRCCALCULATION_DISABLE;
  hspi1.Init.CRCPolynomial = 10;
  if (HAL_SPI_Init(&hspi1) != HAL_OK)
  {
    Error_Handler();
  }
  /* USER CODE BEGIN SPI1_Init 2 */

  /* USER CODE END SPI1_Init 2 */

}

/**
  * @brief TIM1 Initialization Function
  * @param None
  * @retval None
  */
static void MX_TIM1_Init(void)
{

  /* USER CODE BEGIN TIM1_Init 0 */

  /* USER CODE END TIM1_Init 0 */

  TIM_ClockConfigTypeDef sClockSourceConfig = {0};
  TIM_MasterConfigTypeDef sMasterConfig = {0};

  /* USER CODE BEGIN TIM1_Init 1 */

  /* USER CODE END TIM1_Init 1 */
  htim1.Instance = TIM1;
  htim1.Init.Prescaler = 100;
  htim1.Init.CounterMode = TIM_COUNTERMODE_DOWN;
  htim1.Init.Period = 1000;
  htim1.Init.ClockDivision = TIM_CLOCKDIVISION_DIV1;
  htim1.Init.RepetitionCounter = 0;
  htim1.Init.AutoReloadPreload = TIM_AUTORELOAD_PRELOAD_DISABLE;
  if (HAL_TIM_Base_Init(&htim1) != HAL_OK)
  {
    Error_Handler();
  }
  sClockSourceConfig.ClockSource = TIM_CLOCKSOURCE_INTERNAL;
  if (HAL_TIM_ConfigClockSource(&htim1, &sClockSourceConfig) != HAL_OK)
  {
    Error_Handler();
  }
  sMasterConfig.MasterOutputTrigger = TIM_TRGO_RESET;
  sMasterConfig.MasterSlaveMode = TIM_MASTERSLAVEMODE_DISABLE;
  if (HAL_TIMEx_MasterConfigSynchronization(&htim1, &sMasterConfig) != HAL_OK)
  {
    Error_Handler();
  }
  /* USER CODE BEGIN TIM1_Init 2 */

  /* USER CODE END TIM1_Init 2 */

}

/**
  * @brief TIM2 Initialization Function
  * @param None
  * @retval None
  */
static void MX_TIM2_Init(void)
{

  /* USER CODE BEGIN TIM2_Init 0 */

  /* USER CODE END TIM2_Init 0 */

  TIM_ClockConfigTypeDef sClockSourceConfig = {0};
  TIM_MasterConfigTypeDef sMasterConfig = {0};

  /* USER CODE BEGIN TIM2_Init 1 */

  /* USER CODE END TIM2_Init 1 */
  htim2.Instance = TIM2;
  htim2.Init.Prescaler = 99;
  htim2.Init.CounterMode = TIM_COUNTERMODE_DOWN;
  htim2.Init.Period = 999;
  htim2.Init.ClockDivision = TIM_CLOCKDIVISION_DIV1;
  htim2.Init.AutoReloadPreload = TIM_AUTORELOAD_PRELOAD_DISABLE;
  if (HAL_TIM_Base_Init(&htim2) != HAL_OK)
  {
    Error_Handler();
  }
  sClockSourceConfig.ClockSource = TIM_CLOCKSOURCE_INTERNAL;
  if (HAL_TIM_ConfigClockSource(&htim2, &sClockSourceConfig) != HAL_OK)
  {
    Error_Handler();
  }
  sMasterConfig.MasterOutputTrigger = TIM_TRGO_UPDATE;
  sMasterConfig.MasterSlaveMode = TIM_MASTERSLAVEMODE_DISABLE;
  if (HAL_TIMEx_MasterConfigSynchronization(&htim2, &sMasterConfig) != HAL_OK)
  {
    Error_Handler();
  }
  /* USER CODE BEGIN TIM2_Init 2 */

  /* USER CODE END TIM2_Init 2 */

}

/**
  * @brief TIM4 Initialization Function
  * @param None
  * @retval None
  */
static void MX_TIM4_Init(void)
{

  /* USER CODE BEGIN TIM4_Init 0 */

  /* USER CODE END TIM4_Init 0 */

  TIM_ClockConfigTypeDef sClockSourceConfig = {0};
  TIM_MasterConfigTypeDef sMasterConfig = {0};

  /* USER CODE BEGIN TIM4_Init 1 */

  /* USER CODE END TIM4_Init 1 */
  htim4.Instance = TIM4;
  htim4.Init.Prescaler = 99;
  htim4.Init.CounterMode = TIM_COUNTERMODE_DOWN;
  htim4.Init.Period = 1999;
  htim4.Init.ClockDivision = TIM_CLOCKDIVISION_DIV1;
  htim4.Init.AutoReloadPreload = TIM_AUTORELOAD_PRELOAD_DISABLE;
  if (HAL_TIM_Base_Init(&htim4) != HAL_OK)
  {
    Error_Handler();
  }
  sClockSourceConfig.ClockSource = TIM_CLOCKSOURCE_INTERNAL;
  if (HAL_TIM_ConfigClockSource(&htim4, &sClockSourceConfig) != HAL_OK)
  {
    Error_Handler();
  }
  sMasterConfig.MasterOutputTrigger = TIM_TRGO_RESET;
  sMasterConfig.MasterSlaveMode = TIM_MASTERSLAVEMODE_DISABLE;
  if (HAL_TIMEx_MasterConfigSynchronization(&htim4, &sMasterConfig) != HAL_OK)
  {
    Error_Handler();
  }
  /* USER CODE BEGIN TIM4_Init 2 */

  /* USER CODE END TIM4_Init 2 */

}

/**
  * @brief USART2 Initialization Function
  * @param None
  * @retval None
  */
static void MX_USART2_UART_Init(void)
{

  /* USER CODE BEGIN USART2_Init 0 */

  /* USER CODE END USART2_Init 0 */

  /* USER CODE BEGIN USART2_Init 1 */

  /* USER CODE END USART2_Init 1 */
  huart2.Instance = USART2;
  huart2.Init.BaudRate = 115200;
  huart2.Init.WordLength = UART_WORDLENGTH_8B;
  huart2.Init.StopBits = UART_STOPBITS_1;
  huart2.Init.Parity = UART_PARITY_NONE;
  huart2.Init.Mode = UART_MODE_TX_RX;
  huart2.Init.HwFlowCtl = UART_HWCONTROL_NONE;
  huart2.Init.OverSampling = UART_OVERSAMPLING_16;
  if (HAL_UART_Init(&huart2) != HAL_OK)
  {
    Error_Handler();
  }
  /* USER CODE BEGIN USART2_Init 2 */

  /* USER CODE END USART2_Init 2 */

}

/**
  * Enable DMA controller clock
  */
static void MX_DMA_Init(void)
{

  /* DMA controller clock enable */
  __HAL_RCC_DMA2_CLK_ENABLE();

  /* DMA interrupt init */
  /* DMA2_Stream0_IRQn interrupt configuration */
  HAL_NVIC_SetPriority(DMA2_Stream0_IRQn, 0, 0);
  HAL_NVIC_EnableIRQ(DMA2_Stream0_IRQn);

}

/**
  * @brief GPIO Initialization Function
  * @param None
  * @retval None
  */
static void MX_GPIO_Init(void)
{
  GPIO_InitTypeDef GPIO_InitStruct = {0};

  /* GPIO Ports Clock Enable */
  __HAL_RCC_GPIOC_CLK_ENABLE();
  __HAL_RCC_GPIOH_CLK_ENABLE();
  __HAL_RCC_GPIOA_CLK_ENABLE();
  __HAL_RCC_GPIOB_CLK_ENABLE();

  /*Configure GPIO pin Output Level */
  HAL_GPIO_WritePin(GPIOC, S7G_Pin|S7D_Pin|S7E_Pin|S7C_Pin
                          |S7B_Pin|S7F_Pin|S7A_Pin|S7DP_Pin
                          |S7Com4_Pin|S7Com3_Pin|S7Com2_Pin|S7Com1_Pin, GPIO_PIN_RESET);

  /*Configure GPIO pin Output Level */
  HAL_GPIO_WritePin(SPI_NSS_GPIO_Port, SPI_NSS_Pin, GPIO_PIN_SET);

  /*Configure GPIO pin Output Level */
  HAL_GPIO_WritePin(LD2_GPIO_Port, LD2_Pin, GPIO_PIN_RESET);

  /*Configure GPIO pin : B1_Pin */
  GPIO_InitStruct.Pin = B1_Pin;
  GPIO_InitStruct.Mode = GPIO_MODE_IT_FALLING;
  GPIO_InitStruct.Pull = GPIO_NOPULL;
  HAL_GPIO_Init(B1_GPIO_Port, &GPIO_InitStruct);

  /*Configure GPIO pins : S7G_Pin S7D_Pin S7E_Pin S7C_Pin
                           S7B_Pin S7F_Pin S7A_Pin S7DP_Pin
                           S7Com4_Pin S7Com3_Pin S7Com2_Pin S7Com1_Pin */
  GPIO_InitStruct.Pin = S7G_Pin|S7D_Pin|S7E_Pin|S7C_Pin
                          |S7B_Pin|S7F_Pin|S7A_Pin|S7DP_Pin
                          |S7Com4_Pin|S7Com3_Pin|S7Com2_Pin|S7Com1_Pin;
  GPIO_InitStruct.Mode = GPIO_MODE_OUTPUT_PP;
  GPIO_InitStruct.Pull = GPIO_NOPULL;
  GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_LOW;
  HAL_GPIO_Init(GPIOC, &GPIO_InitStruct);

  /*Configure GPIO pin : SPI_NSS_Pin */
  GPIO_InitStruct.Pin = SPI_NSS_Pin;
  GPIO_InitStruct.Mode = GPIO_MODE_OUTPUT_PP;
  GPIO_InitStruct.Pull = GPIO_PULLUP;
  GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_HIGH;
  HAL_GPIO_Init(SPI_NSS_GPIO_Port, &GPIO_InitStruct);

  /*Configure GPIO pin : LD2_Pin */
  GPIO_InitStruct.Pin = LD2_Pin;
  GPIO_InitStruct.Mode = GPIO_MODE_OUTPUT_PP;
  GPIO_InitStruct.Pull = GPIO_NOPULL;
  GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_LOW;
  HAL_GPIO_Init(LD2_GPIO_Port, &GPIO_InitStruct);

  /*Configure GPIO pins : Button1_Pin Button2_Pin */
  GPIO_InitStruct.Pin = Button1_Pin|Button2_Pin;
  GPIO_InitStruct.Mode = GPIO_MODE_IT_RISING;
  GPIO_InitStruct.Pull = GPIO_PULLUP;
  HAL_GPIO_Init(GPIOB, &GPIO_InitStruct);

  /*Configure GPIO pin : ClickInterrupt_Pin */
  GPIO_InitStruct.Pin = ClickInterrupt_Pin;
  GPIO_InitStruct.Mode = GPIO_MODE_IT_RISING;
  GPIO_InitStruct.Pull = GPIO_NOPULL;
  HAL_GPIO_Init(ClickInterrupt_GPIO_Port, &GPIO_InitStruct);

  /* EXTI interrupt init*/
  HAL_NVIC_SetPriority(EXTI0_IRQn, 0, 0);
  HAL_NVIC_EnableIRQ(EXTI0_IRQn);

  HAL_NVIC_SetPriority(EXTI9_5_IRQn, 0, 0);
  HAL_NVIC_EnableIRQ(EXTI9_5_IRQn);

  HAL_NVIC_SetPriority(EXTI15_10_IRQn, 0, 0);
  HAL_NVIC_EnableIRQ(EXTI15_10_IRQn);

}

/* USER CODE BEGIN 4 */
//void HAL_ADC_LevelOutOfWindowCallback(ADC_HandleTypeDef* hadc) {
//	printf("!!!! OUT OF WINDOW INTERRUPT !!!!\r\n");
//}
/* USER CODE END 4 */

/**
  * @brief  This function is executed in case of error occurrence.
  * @retval None
  */
void Error_Handler(void)
{
  /* USER CODE BEGIN Error_Handler_Debug */
  /* User can add his own implementation to report the HAL error return state */
  __disable_irq();
  while (1)
  {
  }
  /* USER CODE END Error_Handler_Debug */
}

#ifdef  USE_FULL_ASSERT
/**
  * @brief  Reports the name of the source file and the source line number
  *         where the assert_param error has occurred.
  * @param  file: pointer to the source file name
  * @param  line: assert_param error line source number
  * @retval None
  */
void assert_failed(uint8_t *file, uint32_t line)
{
  /* USER CODE BEGIN 6 */
  /* User can add his own implementation to report the file name and line number,
     ex: printf("Wrong parameters value: file %s on line %d\r\n", file, line) */
  /* USER CODE END 6 */
}
#endif /* USE_FULL_ASSERT */
