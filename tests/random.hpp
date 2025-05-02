#pragma once
#include <random> 


namespace random{
    
    thread_local std::mt19937_64 gen(std::random_device{}());

    template <typename T>
    typename std::enable_if<std::is_integral<T>::value, T>::type
    randint(T LowNumber, T HighNumber){
        std::uniform_int_distribution<T> distrib(LowNumber, HighNumber);
        return distrib(gen);
    };

    template <typename T>
    typename std::enable_if<std::is_integral<T>::value, T>::type
    randint(T HighNumber){
        std::uniform_int_distribution<T> distrib(0, HighNumber);
        return distrib(gen);
    };

    template <typename T>
    typename std::enable_if<std::is_floating_point<T>::value, T>::type
    randint(T LowNumber, T HighNumber){
        std::uniform_real_distribution<T> distrib(LowNumber, HighNumber);
        return distrib(gen);
    };

    template <typename T>
    typename std::enable_if<std::is_floating_point<T>::value, T>::type
    randint(T HighNumber){
        std::uniform_real_distribution<T> distrib(0, HighNumber);
        return distrib(gen);
    };
}
